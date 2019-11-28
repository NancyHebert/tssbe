import json
import falcon

from data.models.reports_students import reports_students
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin

class Resource(OptionMixin):

    def on_get(self, req, resp):
        """
        @api {get} /reports/students Get data about student profiles and conversations
        @apiName GetStudentsReport
        @apiGroup Reports

        @apiSuccess {Object[]}  student                         List of students
        @apiSuccess {Date}      student.profile_creation        Date student profile was created
        @apisuccess {String}    student.name                    Name as provided in their profile
        @apisuccess {String}    student.email                   as provided, for external students / from Active Directory, for internal students
        @apisuccess {String}    student.level_of_instruction    ("msc"/"phd")
        @apisuccess {String[]}  student.researcher_names        List of researchers the student has contacted
        @apiSuccess {Number}    student.messages_sent           Total number of messages in conversations involving the student

        @apiSuccess {Number}    internal_students_count         Count of students whose usernames don't contain "@" signs
        @apiSuccess {Number}    external_students_count         Count of students whose usernames contain "@" signs
        @apiSuccess {Object[]}  level                           List of levels of instruction
        @apiSuccess {String}    level.level_of_instruction      "msc" or "phd"
        @apiSuccess {Number}    level.count                     Count of students for each level of instruction
        @apiSuccess {Number}    mean_researchers_contacted      Average number of researchers contacted
        @apiSuccess {Number}    median_researchers_contacted    Representative number of researchers contacted
        @apiSuccess {Number}    mean_messages_sent              Average number of messages in conversations
        @apiSuccess {Number}    median_messages_sent            Representative number of messages in conversations
        """

        try:
            result = reports_students.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(result, default=encoder)
