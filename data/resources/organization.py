import falcon
import json

from data.models.organization import organization
from data.resources.decorators.rematch import rematch
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.organizations import schema_update
# from data.resources.decorators.cache import cache_response
# from data.resources.decorators.cache import cache_delete
from cerberus import Validator, errors


class Resource(OptionMixin):

    """
    @api {get} /organizations/:organizations_id Get a organization
    @apiVersion 0.1.0
    @apiName GET /organizations/:organizations_id
    @apiGroup Organizations

    @apiSuccess {Number} id The organization ID
    @apiSuccess {Number} parent_id The parent_id.
    @apiSuccess {Number} organization_types_id The organization_type.
    @apiSuccess {Boolean} is_active If its active.
    @apiSuccess {String} lang The language.
    @apiSuccess {String} name The name.
    @apiSuccess {String} full_path The full path.
    """
    @rematch('organizations_id', '\d+$')
    # @cache_response(60*60*24)
    def on_get(self, req, resp, organizations_id):
        try:
            result = organization.get(organizations_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {delete} /organizations/:organizations_id Delete a organization
    @apiVersion 0.1.0
    @apiName DELETE /organizations/:organizations_id
    @apiGroup Organizations
    """
    @rematch('organizations_id', '\d+$')
    # @cache_delete(['/organizations'])
    def on_delete(self, req, resp, organizations_id):
        try:
            organization.delete(organizations_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_204

    """
    @api {update} /organizations/:organizations_id Update a organization
    @apiVersion 0.1.0
    @apiName UPDATE /organizations/:organizations_id
    @apiGroup Organizations

    @apiParam {Number} [parent_id] The parent_id.
    @apiParam {Number} [organization_types_id] The organization_type.
    @apiParam {Boolean} [is_active] If its active.
    @apiParam {Object} organization_names Organization_names information.
    @apiParam {String{2..2}} [organization_names.lang] The language.
    @apiParam {String{..50}} [organization_names.name] The name.
    @apiParam {String} [organization_names.full_path] The full path.
    """
    @rematch('organizations_id', '\d+$')
    # @cache_delete(['/organizations'])
    def on_put(self, req, resp, organizations_id):
        organizations_json = req.context['doc']

        v = Validator(schema_update)
        if not v.validate(organizations_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            organization.update(organizations_id, organizations_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_204
