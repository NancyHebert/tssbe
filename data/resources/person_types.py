import falcon
import json

from data.models.person_type import person_type
from data.models.person_types import person_types
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.person_types import schema_post
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from cerberus import Validator, errors


class Resource(OptionMixin):
    """
    @api {get} /peopleTypes Get all person types
    @apiVersion 0.1.0
    @apiName GET /peopleTypes
    @apiGroup Person Types

    @apiSuccess {Number} id The Person_Type ID
    @apiSuccess {Number} parent_id The parent id.
    @apiSuccess {Boolean} is_active If its active.
    @apiSuccess {String} lang The language.
    @apiSuccess {String} name The name.
    """
    # @cache_response(60*60*24)
    def on_get(self, req, resp):
        try:
            result = person_types.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {post} /peopleTypes Create a person type
    @apiVersion 0.1.0
    @apiName POST /peopleTypes
    @apiGroup Person Types

    @apiParam {Number} parent_id The parent id.
    @apiParam {Boolean} is_active If its active.
    @apiParam {Object} person_type_names Person_type_names information.
    @apiParam {String{2..2}} person_type_names.lang The language.
    @apiParam {String{..50}} person_type_names.name The name.

    @apiSuccess {Number} id The Person_Type ID
    """
    # @cache_delete()
    def on_post(self, req, resp):
        person_types_json = req.context['doc']

        v = Validator(schema_post)
        if not v.validate(person_types_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            result = person_type.post(person_types_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(result.inserted_primary_key)