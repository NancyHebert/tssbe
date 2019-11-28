import falcon
import json

from data.models.programs import programs
from data.models.program import program
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.programs import schema_post
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from cerberus import Validator, errors


class Resource(OptionMixin):
    """
    @api {get} /programs Get all programs
    @apiVersion 0.1.0
    @apiName GET /programs
    @apiGroup Programs

    @apiSuccess {Number} id The program ID
    @apiSuccess {Number} program_types_id The program_type.
    @apiSuccess {Boolean} is_active If its active.
    @apiSuccess {String} lang The language.
    @apiSuccess {String} name The name.
    """
    # @cache_response(60*60*24)
    def on_get(self, req, resp):
        try:
            result = programs.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {post} /programs Create a program
    @apiVersion 0.1.0
    @apiName POST /programs
    @apiGroup Programs

    @apiParam {Number} program_types_id The program_type.
    @apiParam {Boolean} is_active If its active.
    @apiParam {Object} program_names Program_names information.
    @apiParam {String{2..2}} program_names.lang The language.
    @apiParam {String{..50}} program_names.name The name.
    """
    # @cache_delete()
    def on_post(self, req, resp):
        programs_json = req.context['doc']

        v = Validator(schema_post)
        if not v.validate(programs_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            result = program.post(programs_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(result.inserted_primary_key)
