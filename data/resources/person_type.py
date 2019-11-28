import falcon
import json

from data.models.person_type import person_type
from data.resources.decorators.rematch import rematch
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.person_types import schema_update
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from cerberus import Validator, errors


class Resource(OptionMixin):

    """
    @api {get} /peopleTypes/:person_types_id  Get a person type
    @apiVersion 0.1.0
    @apiName GET /peopleTypes/:person_types_id
    @apiGroup Person Types

    @apiSuccess {Number} id The Person_Type ID
    @apiSuccess {Number} parent_id The parent id.
    @apiSuccess {Boolean} is_active If its active.
    @apiSuccess {String} lang The language.
    @apiSuccess {String} name The name.
    """
    @rematch('person_types_id', '\d+$')
    # @cache_response(60*60*24)
    def on_get(self, req, resp, person_types_id):
        try:
            result = person_type.get(person_types_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {delete} /peopleTypes/:person_types_id  Delete a person type
    @apiVersion 0.1.0
    @apiName DELETE /peopleTypes/:person_types_id
    @apiGroup Person Types
    """
    @rematch('person_types_id', '\d+$')
    # @cache_delete(['/personTypes'])
    def on_delete(self, req, resp, person_types_id):
        try:
            person_type.delete(person_types_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = "The record was successfully deleted"

    """
    @api {update} /peopleTypes/:person_types_id Update a person type
    @apiVersion 0.1.0
    @apiName UPDATE /peopleTypes/:person_types_id
    @apiGroup Person Types

    @apiParam {Number} [parent_id] The parent id.
    @apiParam {Boolean} [is_active] If its active.
    @apiParam {Object} person_type_names Person_type_names information.
    @apiParam {String{2..2}} [person_type_names.lang] The language.
    @apiParam {String{..50}} [person_type_names.name] The name.
    """
    @rematch('person_types_id', '\d+$')
    # @cache_delete(['personTypes'])
    def on_put(self, req, resp, person_types_id):
        person_types_json = req.context['doc']

        v = Validator(schema_update)
        if not v.validate(person_types_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            person_type.update(person_types_id, person_types_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_204
