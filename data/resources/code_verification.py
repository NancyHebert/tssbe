import falcon
import json

from data.models.verification import verification
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
# from cerberus import Validator, errors

class Resource(OptionMixin):

    """
    @api {get} /verifications/:email Get a verification code
    @apiVersion 0.1.0
    @apiName GetVerification
    @apiGroup Student

    """
    def on_get(self, req, resp, email, code):
        try:
            result = verification.get(email, code)
            # TODO: delete code upon verification
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_500,
                                   'Database Error',
                                   'DB exception: %s' % e)
        if (result):
            resp.body = json.dumps(dict(result), default=encoder)
        else:
            resp.status = falcon.HTTP_404 # If no verification code for this email, return FILE_NOT_FOUND


    """
    @api {delete} /verifications/:email Clear out a verification code
    @apiVersion 0.1.0
    @apiName DeleteVerification
    @apiGroup Student

    """
    def on_delete(self, req, resp, email):
        try:
            result = verification.delete(email)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_500,
                                   'Database Error',
                                   'DB exception: %s' % e)
