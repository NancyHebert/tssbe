import falcon
import json

from data.models.researcher import researcher
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from data.resources.decorators.rematch import rematch
from data.resources.schemas.researcher import schema_update
from cerberus import Validator, errors

class Resource(OptionMixin):

    """
    @api {get} /researchers/:uniweb_number Get a researcher
    @apiVersion 0.1.0
    @apiName GetResearcher
    @apiGroup Researcher

    """
    def on_get(self, req, resp, uniweb_number):
        try:
            result = researcher.get(uniweb_number)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_500,
                                   'Database Error',
                                   'DB exception: %s' % e)

        if (result):
            resp.body = json.dumps(dict(result[0]), default=encoder)
        else:
            resp.status = falcon.HTTP_404 # If no researcher, return FILE_NOT_FOUND

    """
    @api {put} /researcher/:uniweb_number Update a researcher
    @apiVersion 0.1.0
    @apiName UpdateResearcher
    @apiGroup Researcher

    """
    def on_put(self, req, resp, uniweb_number):
        researchers_json = req.context['doc']
        v = Validator(schema_update)
        if not v.validate(researchers_json):
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Json Validation Error',
                                   v.errors)

        try:
            researcher.update(uniweb_number, researchers_json)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)
