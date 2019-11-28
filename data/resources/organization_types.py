import falcon
import json

from data.models.organization_types import organization_types
from data.models.organization_type import organization_type
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.organization_types import schema_post
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from cerberus import Validator, errors


class Resource(OptionMixin):

    """
    @api {get} /organizationTypesGet all organization types
    @apiVersion 0.1.0
    @apiName GET /organizationTypes
    @apiGroup Organization Types

    @apiSuccess {Number} id The Organization Types ID
    @apiSuccess {Boolean} is_active If its active.
    @apiSuccess {String} lang The language.
    @apiSuccess {String} name The name.
    """

    # @cache_response(60*60*24)
    def on_get(self, req, resp):
        try:
            result = organization_types.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {post} /organizationTypes Create a organization types
    @apiVersion 0.1.0
    @apiName POST /organizationTypes
    @apiGroup Organization Types

    @apiParam {Boolean} [is_active] If its active.
    @apiParam {Object} organization_type_names Organization_type_names information.
    @apiParam {String{2..2}} organization_type_names.lang The language.
    @apiParam {String{..50}} organization_type_names.name The name.

    @apiSuccess {Number} id The organization_types ID.
    """
    # @cache_delete()
    def on_post(self, req, resp):
        organization_types_json = req.context['doc']

        v = Validator(schema)
        if not v.validate(organization_types_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            result = organization_type.post(organization_types_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(result.inserted_primary_key)
