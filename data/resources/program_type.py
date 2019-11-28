import falcon
import json

from data.models.program_type import program_type
from data.resources.decorators.rematch import rematch
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.program_types import schema_update
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from cerberus import Validator, errors


class Resource(OptionMixin):
    """
    @api {get} /programsTypes/:program_types_id Get a program type
    @apiVersion 0.1.0
    @apiName GET /programsTypes/:program_types_id
    @apiGroup Program Types

    @apiSuccess {Number} id The program type ID
    @apiSuccess {Boolean} is_active If its active.
    @apiSuccess {String} lang The language.
    @apiSuccess {String} name The name.
    """
    @rematch('program_types_id', '\d+$')
    # @cache_response(60*60*24)
    def on_get(self, req, resp, program_types_id):
        try:
            result = program_type.get(program_types_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {delete} /programsTypes/:program_types_id Delete a program type
    @apiVersion 0.1.0
    @apiName DELETE /programsTypes/:program_types_id
    @apiGroup Program Types
    """
    @rematch('program_types_id', '\d+$')
    # @cache_delete(['/programTypes'])
    def on_delete(self, req, resp, program_types_id):
        try:
            program_type.delete(program_types_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = "The record was successfully deleted"

    """
    @api {update} /programsTypes/:program_types_id Update a program type
    @apiVersion 0.1.0
    @apiName Update /programsTypes/:program_types_id
    @apiGroup Program Types

    @apiParam {Boolean} [is_active] If its active.
    @apiParam {Object} program_type_names Program_type_names information.
    @apiParam {String{2..2}} [program_type_names.lang] The language.
    @apiParam {String{..50}} [program_type_names.name] The name.
    """
    @rematch('program_types_id', '\d+$')
    # @cache_delete(['/programTypes'])
    def on_put(self, req, resp, program_types_id):
        program_types_json = req.context['doc']

        v = Validator(schema_update)
        if not v.validate(program_types_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            program_type.update(program_types_id, program_types_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_204
