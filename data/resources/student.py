import json
import falcon

from data.models.student import student
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
# from data.resources.decorators.rematch import rematch
from data.resources.schemas.student import schema_update
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from cerberus import Validator, errors

class Resource(OptionMixin):

    # @cache_response(60*60*24)
    def on_get(self, req, resp, username):
        """
        @api {get} /students/:username  Get the student profile with this username
        @apiName GetStudent
        @apiGroup Student

        @apiParam {String}      username                For internal students: Active Directory username. For external students: email address (URLencoded).

        @apiSuccess {Number}    id                      Unique internal identifier
        @apiSuccess {String}    name                    Full name of student
        @apiSuccess {String}    email                   Student email, used for notifications
        @apiSuccess {Number}    program_code            Code, per /gs_programs service
        @apiSuccess {String}    level_of_instruction    "msc" or "phd"
        @apiSuccess {Date}      date_created            Date the profile was created
        @apiSuccess {String}    is_active               (Reserved for future use)
        """

        try:
            result = student.get(username)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e)

        if result is not None:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(dict(result), default=encoder) # [dict(row) for row in result][0] # There should just be one response
        else:
            resp.status = falcon.HTTP_404

    # """
    # @api {delete} /students/:username Delete a student
    # @apiVersion 0.1.0
    # @apiName DELETE /students/:username
    # @apiGroup Student
    # """
    # # @cache_delete(['/students'])
    # def on_delete(self, req, resp, username):
    #     try:
    #         student.delete(username)
    #     except Exception as e:
    #         raise falcon.HTTPError(falcon.HTTP_400, 'Error', e)

    #     resp.status = falcon.HTTP_204

    def on_put(self, req, resp, username):
        """
        @api {put} /students/:username  Update a student profile
        @apiName UpdateStudent
        @apiGroup Student

        @apiParam {String}  username                For internal students: Active Directory username. For external students: email address (URLencoded).
        @apiParam {String}  name                    Full name of student
        @apiParam {String}  email                   Student email, used for notifications
        @apiParam {Number}  program_code            Code, per /gs_programs service
        @apiParam {String}  level_of_instruction    "msc" or "phd"
        """

        req_json = req.context['doc']
        v = Validator(schema_update)
        if not v.validate(req_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            result = student.update(username, req_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e)

        if result is not None:
            resp.status = falcon.HTTP_204
        else:
            resp.status = falcon.HTTP_404


    # """
    # @api {post} /student Update a student
    # @apiVersion 0.1.0
    # @apiName POST /student
    # @apiGroup Student

    # @apiSuccess {Number} student_id The Student ID
    # """
    # @rematch('student_id', '\d+$')
    # def on_post(self, req, resp, student_id):
    #     req_json = req.context['doc']

    #     v = Validator(schema_post)
    #     if not v.validate(req_json):
    #         raise falcon.HTTPError(falcon.HTTP_400,json.dumps([dict(r) for r in result], default=encoder)
    #                                'Json Validation Error',
    #                                v.errors)

    #     try:
    #         result = student.postbyid(req_json)
    #         if result.is_insert:
    #             student_id = result.inserted_primary_key[0]
    #         else:
    #             student_id=[dict(r) for r in result][0]["id"]
    #     except Exception as e:
    #         raise falcon.HTTPError(falcon.HTTP_400,
    #                                'Database Error',
    #                                'DB exception: %s' % e)

    #     resp.status = falcon.HTTP_201
    #     resp.body = json.dumps(student_id)
