#!/usr/bin/env python3
"""
    tss_be.py: This is the main program. It is a simple service that provides services to get and
    persist data related to Thesis Supervor Search.

    To learn more about the launch options, read the Gunicorn documentation
    at: http://docs.gunicorn.org/en/stable/

    The launch command is contained in the dockerfile.
"""

__author__      = "Jim Cassidy, Don Farmer, Kivi Shapiro"
__copyright__   = "Copyright 2017 by The University of Ottawa, faculty of Medicine."
__license__     = "TBD"
__status__      = "Development"
__version__     = "0.01.01"

# Standard imports
import json
import os
from time import sleep
import falcon
from falcon_cors import CORS
from sqlalchemy import create_engine, exc
from falcon_multipart.middleware import MultipartMiddleware
from utils.json_utils import JSONTranslator
import socket

# Set up database
sleep(15)
engine = create_engine('postgresql+psycopg2cffi://odin:y0uguysr0ck@db', isolation_level='AUTOCOMMIT')
conn = engine.connect()
conn.execute('commit;') # This line is needed: see http://stackoverflow.com/a/8977109/5516499

try:
    conn.execute("CREATE DATABASE midgard TEMPLATE template0;")
    conn.execute('commit;')
except exc.ProgrammingError: # Catch and ignore the error that is thrown when the database already exists
    pass

os.system('./migrate.sh')

# More custom imports now that database is set up
from data.resources import \
    cvs, cv, \
    gs_programs, \
    conversations, conversation, conversation_token, \
    reports_profiles_by_month, reports_students, reports_supervisors, \
    reports_profiles_by_month_xlsx, reports_students_xlsx, reports_supervisors_xlsx, \
    researchers, researcher, \
    roles, \
    students, student, \
    transcripts, transcript, \
    code_verification, code_generation
    # configuration, \
    # documents, \
    # emails, \
    # organizations, organization, \
    # organization_types, organization_type, \
    # people, \
    # person, \
    # person_types, person_type, \
    # programs, program, \
    # program_types, program_type, \

# falcon.API instances are callable WSGI apps
cors = CORS(allow_all_origins=True, allow_all_headers=True, allow_all_methods=True)
app = falcon.API(middleware=[
    cors.middleware,
    MultipartMiddleware(),
    JSONTranslator()
])

# Set up "/heartbeat", to check whether server is up
class HeartBeat:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': 'Server Up, Captain',
            'author': 'Scotty',
            'hostname': socket.gethostname()
        }

        resp.body = json.dumps(quote)

app.add_route("/heartbeat", HeartBeat())

# Set up other routes
app.add_route('/gs_programs', gs_programs.Resource())
app.add_route('/conversations', conversations.Resource())
app.add_route('/conversations/{id}', conversation.Resource())
app.add_route('/conversations/token/{token}', conversation_token.Resource())
app.add_route('/reports/profiles-by-month/start/{start}/end/{end}', reports_profiles_by_month.Resource())
app.add_route('/reports/profiles-by-month/start/{start}/end/{end}/profiles-by-month.xlsx', reports_profiles_by_month_xlsx.Resource())
app.add_route('/reports/students', reports_students.Resource())
app.add_route('/reports/students/students.xlsx', reports_students_xlsx.Resource())
app.add_route('/reports/supervisors', reports_supervisors.Resource())
app.add_route('/reports/supervisors/supervisors.xlsx', reports_supervisors_xlsx.Resource())
app.add_route('/researchers', researchers.Resource())
app.add_route('/researchers/{uniweb_number}', researcher.Resource())
app.add_route('/roles/{username}', roles.Resource())
app.add_route('/students', students.Resource())
app.add_route('/students/{username}', student.Resource())
app.add_route('/students/{username}/cvs', cvs.Resource())
app.add_route('/students/{username}/cvs/{filename}', cv.Resource())
app.add_route('/students/{username}/transcripts', transcripts.Resource())
app.add_route('/students/{username}/transcripts/{filename}', transcript.Resource())
app.add_route('/verifications/{template}/{email}', code_generation.Resource())
app.add_route('/verifications/email/{email}/code/{code}', code_verification.Resource())
# Not-so-good routes
# app.add_route('/emails', emails.Resource())
# app.add_route('/organizations', organizations.Resource())
# app.add_route('/organizations/{organizations_id}', organization.Resource())
# app.add_route('/organizationTypes', organization_types.Resource())
# app.add_route('/organizationTypes/{organization_types_id}', organization_type.Resource())
# app.add_route('/people', people.Resource())
# app.add_route('/people/{people_id}', person.Resource())
# app.add_route('/peopleTypes', person_types.Resource())
# app.add_route('/peopleTypes/{person_types_id}', person_type.Resource())
# app.add_route('/programs', programs.Resource())
# app.add_route('/programs/{programs_id}', program.Resource())
# app.add_route('/programTypes', program_types.Resource())
# app.add_route('/programTypes/{program_types_id}', program_type.Resource())
# app.add_route('/students/view/profile_counts', students.Resource())
# app.add_route('/students/view/researcher_response', students.Resource())
# app.add_route('/students/view/student_signups', students.Resource())

# # configuration webhook
#app.add_route('/configuration', configuration.Resource())
#
# #
# document_collection = documents.Collection()
# document = documents.Item()
# #
# app.add_route('/students/{student_id}/documents', document_collection)
# app.add_route('/students/{student_id}/documents/{name}', document)
