import json
import falcon

from data.models.reports_supervisors import reports_supervisors
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin

class Resource(OptionMixin):

    def on_get(self, req, resp):
        """
        @api {get} /reports/supervisors Get data about how quickly supervisors are responding
        @apiName GetSupervisorsReport
        @apiGroup Reports

        @apiSuccess {Object[]}  supervisor                      List of supervisors
        @apiSuccess {String}    supervisor.uniweb_number        ID from the UNIWeb system
        @apiSuccess {String}    supervisor.name                 Full name (snapshotted at time of conversations)
        @apiSuccess {Number}    supervisor.mean_response_time   Average time to respond to an initial inquiry
        @apiSuccess {Number}    supervisor.median_response_time Representative time to respond to an initial inquiry
        @apiSuccess {Number}    supervisor.unreturned_contacts  Number of initial inquiries without supervisor response
        """

        try:
            result = reports_supervisors.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps([dict(r) for r in result], default=encoder)
