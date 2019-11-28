import falcon
import json

from data.models.program import program
from data.resources.decorators.rematch import rematch
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.programs import schema_update
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from cerberus import Validator, errors


class Resource(OptionMixin):
    """
    @api {get} /programs/:programs_id Get a program
    @apiVersion 0.1.0
    @apiName GET /programs/:programs_id
    @apiGroup Programs

    @apiSuccess {Number} id The program ID
    @apiSuccess {Number} program_types_id The program_type.
    @apiSuccess {Boolean} is_active If its active.
    @apiSuccess {String} lang The language.
    @apiSuccess {String} name The name.
    """
    @rematch('programs_id', '\d+$')
    # @cache_response(60*60*24)
    def on_get(self, req, resp, programs_id):
        try:
            result = program.get(programs_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {delete} /programs/:programs_id Delete a program
    @apiVersion 0.1.0
    @apiName DELETE /programs/:programs_id
    @apiGroup Programs
    """
    @rematch('programs_id', '\d+$')
    # @cache_delete(['/programs'])
    def on_delete(self, req, resp, programs_id):
        try:
            program.delete(programs_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = "The record was successfully deleted"

    """
    @api {update} /programs/:programs_id Update a program
    @apiVersion 0.1.0
    @apiName UPDATE /programs/:programs_id
    @apiGroup Programs

    @apiParam {Number} [program_types_id] The program_type.
    @apiParam {Boolean} [is_active] If its active.
    @apiParam {Object} program_names Program_names information.
    @apiParam {String{2..2}} [program_names.lang] The language.
    @apiParam {String{..50}} [program_names.name] The name.
    """
    @rematch('programs_id', '\d+$')
    # @cache_delete(['/programs'])
    def on_put(self, req, resp, programs_id):
        programs_json = req.context['doc']

        v = Validator(schema_update)
        if not v.validate(programs_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            program.update(programs_id, programs_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_204
