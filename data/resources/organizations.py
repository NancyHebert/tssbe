import falcon
import json

from data.models.organization import organization
from data.models.organizations import organizations
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.organizations import schema_post
# from data.resources.decorators.cache import cache_response
# from data.resources.decorators.cache import cache_delete
from cerberus import Validator, errors


class Resource(OptionMixin):

    """
    @api {get} /organizations Get all organizations
    @apiVersion 0.1.0
    @apiName GET /organizations
    @apiGroup Organizations

    @apiSuccess {Number} id The organization ID
    @apiSuccess {Number} parent_id The parent_id.
    @apiSuccess {Number} organization_types_id The organization_type.
    @apiSuccess {Boolean} is_active If its active.
    @apiSuccess {String}lang The language.
    @apiSuccess {String} name The name.
    @apiSuccess {String} full_path The full path.
    """
    # @cache_response(60*60*24)
    def on_get(self, req, resp):
        try:
            result = organizations.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {post} /organizations Create a organization
    @apiVersion 0.1.0
    @apiName POST /organizations
    @apiGroup Organizations

    @apiParam {Number} parent_id The parent_id.
    @apiParam {Number} organization_types_id The organization_type.
    @apiParam {Boolean} is_active If its active.
    @apiParam {Object} organizsation_names Organization_names information.
    @apiParam {String{2..2}} organization_names.lang The language.
    @apiParam {String{..50}} organization_names.name The name.
    @apiParam {String} organization_names.full_path The full path.

    @apiSuccess {Number} id The Organization ID
    """
    # @cache_delete()
    def on_post(self, req, resp):
        organizations_json = req.context['doc']

        v = Validator(schema_post)
        if not v.validate(organizations_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            result = organization.post(organizations_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_201
        resp.body = json.dumps(result.inserted_primary_key)
