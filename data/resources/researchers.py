import falcon
import json

from data.models.researchers import researchers
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from cerberus import Validator, errors

class Resource(OptionMixin):

    """
    @api {get} /researchers/ Get availability for all researchers
    @apiName GetResearchers
    @apiGroup Researcher

    """
    def on_get(self, req, resp):
        try:
            results = researchers.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_500,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.body = json.dumps([dict(row) for row in results], default=encoder)
