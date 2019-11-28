import json
import os
import uuid
import re

from urllib.parse import quote_plus
import falcon
import requests

from cerberus import Validator, errors

from config.settings import config
from data.models.conversation import conversation
from data.models.conversations import conversations
from data.models.student import student
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.conversations import schema_post
# from data.resources.decorators.cache import cache_response
# from data.resources.decorators.cache import cache_delete
from data.resources.emails.email import Email
# from data.models.gs_program import gs_program

class Resource(OptionMixin):

    def on_get(self, req, resp):
        """
        @api {get} /messages Get all messages
        @apiName GetMessages
        @apiGroup Conversation
        """
        try:
            result = conversations.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(row) for row in result], default=encoder)


    def on_post(self, req, resp):
        """
        @api {post} /messages Adds a new message to the collection
        @apiName NewMessage
        @apiGroup Conversation
        @apiSuccess {Number} conversation_id The Conversation ID
        """

        try:
            conversations_json = req.context['doc']
        except KeyError:
            raise falcon.HTTPBadRequest(
                'Missing info',
                'Could not find the request body.')

        v = Validator(schema_post)
        if not v.validate(conversations_json):
            raise falcon.HTTPError(
                falcon.HTTP_400,
                'JSON validation error',
                v.errors)

        # Create token
        token = uuid.uuid4() # Random uuid
        conversations_json['token'] = str(token)

        if conversations_json['is_from_student']:
            # Message from student. Is it a followup?
            try:
                messages_in_conversation = conversations.getByStudentAndResearcher(
                    conversations_json['student_username'],
                    conversations_json['researcher_uniweb_number'])
            except Exception as e:
                raise falcon.HTTPError(
                    falcon.HTTP_400,
                    'Error while finding conversation for student {' \
                    + conversations_json['student_username'] \
                    + '} with researcher {'  \
                    + conversations_json['researcher_uniweb_number'] \
                    + '}',
                    'Exception: %s' % e)
            message_count = len(messages_in_conversation)

            if message_count == 0:
                # No previous messages. This is an initial message.
                conversation_id = student_initial(conversations_json)

            elif message_count == 1:
                # Student has saved (and possibly sent) an initial message.
                message = messages_in_conversation[0]

                if message['is_draft']:
                    # The existing message is a draft. Delete it and replace with this one.
                    try:
                        result = conversation.delete(message['id'])
                    except Exception as e:
                        raise falcon.HTTPError(
                            falcon.HTTP_500,
                            'Unable to delete existing message',
                            'Exception: %s' % e)

                    conversation_id = student_initial(conversations_json)

                else:
                    # The existing message is not a draft. Student cannot save
                    # or send any more messages until researcher responds.
                    raise falcon.HTTPError(
                        falcon.HTTP_400,
                        'Cannot save message',
                        'Student must wait for researcher to respond')

            else:
                # Message count is >1, so student has sent a message and researcher has responded.

                if conversations_json['is_draft']:
                    # Drafts can only be saved for initial messages.
                    raise falcon.HTTPError(
                        falcon.HTTP_400,
                        'Cannot save draft',
                        'Conversation already includes %s messages' % message_count)

                else:
                    # Followup message from student. Send notification to researcher.
                    conversation_id = student_followup(conversations_json)

        else:
            # Followup message from professor. Send notification to student.
            conversation_id = researcher_followup(conversations_json)

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(conversation_id)


def generate_links(student_username, foldername):
    """Create HTML links for files in a folder (cvs or transcripts)"""
    storage_path = config["storage"]["storage_path"]
    student_folder = storage_path +"/students/" + student_username
    try:
        file_list = os.listdir(student_folder + "/" + foldername)
    except FileNotFoundError as e:
        file_list = []
    links = ""
    first_time_through_loop = True
    for filename in file_list:
        if first_time_through_loop:
            first_time_through_loop = False
        else:
            links += ", "
        links += "<a href='https://tss-be.med.uottawa.ca/students/" \
            + quote_plus(student_username) + "/" \
            + quote_plus(foldername)  + "/" \
            + quote_plus(filename) + "'>" \
            + filename + "</a>"
    return links


def save_message(conversations_json):
    """Save message to the database"""
    try:
        result = conversation.post(conversations_json)
    except Exception as e:
        raise falcon.HTTPError(
            falcon.HTTP_500,
            'Unable to save message',
            'Exception: %s' % e)

    if result.is_insert:
        conversation_id = result.inserted_primary_key[0]
    else:
        conversation_id = [dict(r) for r in result][0]["id"]

    return conversation_id


def setup_email_args(conversations_json):
    """Common functionality for notification sending"""

    email_args = {}
    email_args['message'] = conversations_json['body']
    email_args['token'] = conversations_json['token']

    return email_args


def get_researcher_email(researcher_uniweb_number):
    """Get researcher email from UNIWeb"""
    try:
        result = requests.get(config["UNIWeb"]["host"] + '/professors/' \
            + str(researcher_uniweb_number))
        researcher_json = json.loads(result.content.decode('utf-8'))
    except Exception as e:
        raise falcon.HTTPError(
            falcon.HTTP_500,
            'UNIWeb connection error',
            'exception: %s' % e)

    # Check if researcher exists in UNIWeb
    if 'error' in researcher_json:
        raise falcon.HTTPError(
            falcon.HTTP_400,
            'Researcher {%s} does not exist' % researcher_uniweb_number)

    # Check if email field exists in UNIWeb data, and validate it
    email_exists = True
    if 'email' in researcher_json['membership_information'] and \
            re.match(r"[^@]+@[^@]+\.[^@]+", researcher_json['membership_information']['email']):
        to_addrs = researcher_json['membership_information']['email']
    else:
        print('missing or malformed email addrs from UNIWeb: ', str(researcher_uniweb_number))
        to_addrs = config["email"]["tss_admin_addrs"]
        email_exists = False

    return (to_addrs, email_exists)


def researcher_followup(conversations_json):
    """Process followup message from researcher"""

    conversation_id = save_message(conversations_json)

    # Notify student
    template = 'researcher_notification_to_student'

    email_args = setup_email_args(conversations_json)
    email_args['researcher_name'] = conversations_json['researcher_name']

    # Get student email address
    student_object = student.get(conversations_json['student_username'])
    to_addrs = student_object['email']

    # print("sending to %s" % to_addrs)
    # print("template: %s" % template)
    # print(email_args)

    notification_email = Email(template, **email_args)
    notification_email.send(to_addrs)

    return conversation_id


def student_followup(conversations_json):
    """Process followup message from student"""

    conversation_id = save_message(conversations_json)

    # Notify researcher
    template = 'student_subsequent_notification_to_researcher'

    email_args = setup_email_args(conversations_json)
    email_args['student_name'] = conversations_json['student_name']

    # Get researcher email address
    (to_addrs, email_exists) = get_researcher_email(conversations_json['researcher_uniweb_number'])
    if not email_exists:
        email_args['missing_researcher_email'] = '--> *** '\
            + 'Missing researcher email in UNIWeb: ' \
            + conversations_json['researcher_name'] + ' *** <!--'

    # print("sending to %s" % to_addrs)
    # print("template: %s" % template)
    # print(email_args)

    notification_email = Email(template, **email_args)
    notification_email.send(to_addrs)

    return conversation_id


def student_initial(conversations_json):
    """Process initial message from student"""

    conversation_id = save_message(conversations_json)

    if not conversations_json['is_draft']:

        # Notify researcher
        template = 'student_first_notification_to_researcher'

        email_args = setup_email_args(conversations_json)
        email_args['student_name'] = conversations_json['student_name']

        # Students can send an initial message even without a complete profile
        try:
            level_en = conversations_json['level_of_instruction_en']
            level_fr = conversations_json['level_of_instruction_fr']
        except KeyError:
            level_en = ""
            level_fr = ""
        email_args['level_en'] = level_en
        email_args['level_fr'] = level_fr

        try:
            admitted_en = conversations_json['admitted_en']
            admitted_fr = conversations_json['admitted_fr']
        except KeyError:
            admitted_en = ""
            admitted_fr = ""
        email_args['admitted_en'] = admitted_en
        email_args['admitted_fr'] = admitted_fr

        try:
            program_en = conversations_json['program_en']
            program_fr = conversations_json['program_fr']
        except KeyError:
            program_en = ""
            program_fr = ""
        email_args['program_en'] = program_en
        email_args['program_fr'] = program_fr

        email_args['cvs_links'] = generate_links(conversations_json['student_username'], "cvs")
        email_args['transcripts_links'] = generate_links(conversations_json['student_username'], "transcripts")

        # Get researcher email address
        (to_addrs, email_exists) = get_researcher_email(conversations_json['researcher_uniweb_number'])
        if not email_exists:
            email_args['missing_researcher_email'] = '--> *** '\
                + 'Missing researcher email in UNIWeb: ' \
                + conversations_json['researcher_name'] + ' *** <!--'

        # print("sending to %s" % to_addrs)
        # print("template: %s" % template)
        # print(email_args)

        notification_email = Email(template, **email_args)
        notification_email.send(to_addrs)

    return conversation_id
