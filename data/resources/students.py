import falcon
import json

from data.models.students import students
from data.models.student import student
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from data.resources.schemas.students import schema_post
from cerberus import Validator, errors


class Resource(OptionMixin):

    """
    @api {get} /students Get all students
    @apiVersion 0.1.0
    @apiName GET /students
    @apiGroup Student

    """
    # @cache_response(60*60*24)
    def on_get(self, req, resp):
        try:
            result = students.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(row) for row in result], default=encoder)

    """
    @api {post} /students Adds a new student to the collection
    @apiVersion 0.1.0
    @apiName POST /students
    @apiGroup Student

    @apiSuccess {Number} student_id The Student ID
    """

    def on_post(self, req, resp):

        try:
            students_json = req.context['doc']

        except KeyError:
            raise falcon.HTTPBadRequest(
                'Missing info',
                'Could not find the request body.')

        v = Validator(schema_post)
        if not v.validate(students_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'JSON validation error',
                                   v.errors)

        try:
            result = student.post(students_json)
            if result.is_insert:
                students_id = result.inserted_primary_key[0]
            else:
                students_id=[dict(r) for r in result][0]["id"]
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(students_id)

    
