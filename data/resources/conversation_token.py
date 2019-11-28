import falcon
import json

from data.models.conversation import conversation
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin

class Resource(OptionMixin):

    def on_get(self, req, resp, token):
        try:
            result = conversation.getByToken(token)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_500,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(dict(result), default=encoder)

