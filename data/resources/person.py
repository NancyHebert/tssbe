import falcon
import json

from data.models.person import person
from data.resources.decorators.rematch import rematch
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.people import schema_update
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from cerberus import Validator, errors


class Resource(OptionMixin):

    """
    @api {get} /people/:people_id Get a person
    @apiVersion 0.1.0
    @apiName GET /people/:people_id
    @apiGroup People

    @apiSuccess {Number} id The Person ID
    @apiSuccess {String} first_name First name
    @apiSuccess {String} middle_initial Middle initial.
    @apiSuccess {String} last_name Last name.
    @apiSuccess {Date} date_of_birth Date of birth.
    @apiSuccess {Number} person_types_id Person type id
    """
    @rematch('people_id', '\d+$')
    # @cache_response(60*60*24)
    def on_get(self, req, resp, people_id):
        try:
            result = person.get(people_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {delete} /people/:people_id Delete a person
    @apiVersion 0.1.0
    @apiName DELETE /people/:people_id
    @apiGroup People
    """
    @rematch('people_id', '\d+$')
    # @cache_delete(['/people'])
    def on_delete(self, req, resp, people_id):
        try:
            person.delete(people_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = "The record was successfully deleted"

    """
    @api {update} /people/:people_id Update a person
    @apiVersion 0.1.0
    @apiName UPDATE /people/:people_id
    @apiGroup People

    @apiParam {String{..50}} [first_name] First name
    @apiParam {String{1..1}} [middle_initial] Middle initial.
    @apiParam {String{..50}} [last_name] Last name.
    @apiParam {Date} [date_of_birth] Date of birth.
    @apiParam {Number} [person_types_id] Person type id
    """
    @rematch('people_id', '\d+$')
    # @cache_delete(['/people'])
    def on_put(self, req, resp, people_id):
        people_json = req.context['doc']

        v = Validator(schema_update)
        if not v.validate(people_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            person.update(people_id, people_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_204
