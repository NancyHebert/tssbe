import json
import falcon

from data.resources.utils.options_mixin import OptionMixin
from data.resources.decorators.rematch import rematch
from data.models.verification import verification
from data.resources.schemas.emails import schema_post
from cerberus import Validator, errors

from utils import wf
from datetime import datetime, timezone

class Resource(OptionMixin):

    """
    @api {post} /emails Send an email
    @apiVersion 0.1.0
    @apiName POST /emails
    @apiGroup Email

    @apiSuccess {} 
    """
    def on_post(self, req, resp):
        try:
            body = req.stream.read()
        except Exception:
            raise falcon.HTTPError(falcon.HTTP_748,
                                   'Read Error',
                                   'Could not read the request body.')

        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid Json document is required.')

        try:
            email_json = json.loads(body.decode('utf-8'))
        except ValueError:
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed Json',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')


        v = Validator(schema_post)
        if not v.validate(email_json):
            raise falcon.HTTPError(falcon.HTTP_753,
                'Json Validation Error',
                v.errors)

        try:
            now = datetime.now(timezone.utc).isoformat()
            w = wf.workflow()
            w.send_email(email_json["from"],email_json["to"], email_json["subject"], email_json["message"], now)

        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_500,
                                   'Workflow Engine Error',
                                   'Unable to send the email: %s' % e)

        resp.status = falcon.HTTP_200


    @rematch('email', '\d+$')
    # @cache_response(60*60*24)
    def on_get(self, req, resp, email):
        try:
            result = verification.get(email)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400,
                                   'Database Error',
                                   'DB exception: %s' % e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)

