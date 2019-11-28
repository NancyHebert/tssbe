import falcon
import json

from data.models.program_types import program_types
from data.models.program_type import program_type
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.program_types import schema_post
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from cerberus import Validator, errors


class Resource(OptionMixin):
    """
    @api {get} /programTypes Get all program types
    @apiVersion 0.1.0
    @apiName GET /programsTypes
    @apiGroup Program Types

    @apiSuccess {Number} id The program type ID
    @apiSuccess {Boolean} is_active If its active.
    @apiSuccess {String} lang The language.
    @apiSuccess {String} name The name.
    """
    # @cache_response(60*60*24)
    def on_get(self, req, resp):
        try:
            result = program_types.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {post} /programsTypes Create a program type
    @apiVersion 0.1.0
    @apiName POST /programsTypes
    @apiGroup Program Types

    @apiParam {Boolean} is_active If its active.
    @apiParam {Object} program_type_names Program_type_names information.
    @apiParam {String{2..2}} program_type_names.lang The language.
    @apiParam {String{..50}} program_type_names.name The name.

    @apiSuccess {Number} id The Program_Type ID
    """
    # @cache_delete()
    def on_post(self, req, resp):
        program_types_json = req.context['doc']

        v = Validator(schema_post)
        if not v.validate(program_types_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            result = program_type.post(program_types_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(result.inserted_primary_key)
