import falcon
import json

from data.models.gs_programs import gs_programs
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from data.resources.schemas.people import schema_post
from cerberus import Validator, errors


class Resource(OptionMixin):

    """
    @api {get} /people Get all people
    @apiVersion 0.1.0
    @apiName GET /people
    @apiGroup People

    @apiSuccess {Number} id The Person ID
    @apiSuccess {String} first_name First name
    @apiSuccess {String} middle_initial Middle initial.
    @apiSuccess {String} last_name Last name.
    @apiSuccess {Date} date_of_birth Date of birth.
    @apiSuccess {Number} person_types_id Person type id
    """
    def on_get(self, req, resp):
        try:
            result = gs_programs.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {post} /people Create a person
    @apiVersion 0.1.0
    @apiName POST /people
    @apiGroup People

    @apiParam {String{..50}} first_name First name
    @apiParam {String{1..1}} [middle_initial] Middle initial.
    @apiParam {String{..50}} last_name Last name.
    @apiParam {Date} date_of_birth Date of birth.
    @apiParam {Number} person_types_id Person type id

    @apiSuccess {Number} id The Person ID
    """
    # @cache_delete()
    def on_post(self, req, resp):
        people_json = req.context['doc']

        v = Validator(schema_post)
        if not v.validate(people_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            result = person.post(people_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(result.inserted_primary_key)
