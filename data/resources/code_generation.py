import falcon
# import json

from data.models.verification import verification
# from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
# from cerberus import Validator, errors

class Resource(OptionMixin):

    """
    @api {post} /verification/:email Create or resend a verification code
    @apiVersion 0.1.0
    @apiName CreateVerification
    @apiGroup Student

    """
    def on_post(self, req, resp, template, email):
        try:
            verification.post(template, email)
            resp.status = falcon.HTTP_201
            # resp.body = json.dumps(dict(result[0]), default=encoder)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_500,
                                   'Database Error',
                                   'DB exception: %s' % e)


