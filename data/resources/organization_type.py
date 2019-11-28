import falcon
import json

from data.models.organization_type import organization_type
from data.resources.decorators.rematch import rematch
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.schemas.organization_types import schema_update
# from data.resources.decorators.cache import cache_delete
# from data.resources.decorators.cache import cache_response
from cerberus import Validator, errors


class Resource(OptionMixin):

    """
    @api {get} /organizationTypes/:organization_types_id Get a organization types
    @apiVersion 0.1.0
    @apiName GET /organizationTypes/:organization_types_id
    @apiGroup Organization Types

    @apiSuccess {Number} id The Organization Types ID
    @apiSuccess {Boolean} is_active If its active.
    @apiSuccess {String} lang The language.
    @apiSuccess {String} name The name.
    """
    @rematch('organization_types_id', '\d+$')
    # @cache_response(60*60*24)
    def on_get(self, req, resp, organization_types_id):
        try:
            result = organization_type.get(organization_types_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

    """
    @api {delete} /organizationTypes/:organization_types_id Delete a organization types
    @apiVersion 0.1.0
    @apiName DELETE /organizationTypes/:organization_types_id
    @apiGroup Organization Types
    """
    @rematch('organization_types_id', '\d+$')
    # @cache_delete(['/organizationTypes'])
    def on_delete(self, req, resp, organization_types_id):
        try:
            organization_type.delete(organization_types_id)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = "The record was successfully deleted"

    """
    @api {update} /organizationTypes/:organization_types_id Update a organization types
    @apiVersion 0.1.0
    @apiName UPDATE /organizationTypes/:organization_types_id
    @apiGroup Organization Types

    @apiParam {Boolean} [is_active] If its active.
    @apiParam {Object} organization_type_names Organization_type_names information.
    @apiParam {String{2..2}} [organization_type_names.lang] The language.
    @apiParam {String{..50}} [organization_type_names.name] The name.
    """
    @rematch('organization_types_id', '\d+$')
    # @cache_delete(['/organizationTypes'])
    def on_put(self, req, resp, organization_types_id):
        organization_types_json = req.context['doc']
        
        v = Validator(schema_update)
        if not v.validate(organization_types_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            organization_type.put(organization_types_id, organization_types_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_204
