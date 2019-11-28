import json
import falcon

from data.models.reports_profiles_by_month import reports_profiles_by_month
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin

class Resource(OptionMixin):

    def on_get(self, req, resp, start, end):
        """
        @api {get} /reports/profiles-by-month/start/:start/end/:end Get counts of profiles created each month between start date and end date inclusive
        @apiName GetProfilesByMonthReport
        @apiGroup Reports

        @apiParam {Date}        start       Start of date range to consider, in yyyy-mm-dd format
        @apiParam {Date}        end         End of date range to consider, in yyyy-mm-dd format

        @apiSuccess {Object[]}  datum       List of data points
        @apiSuccess {Date}      datum.month Month to consider (shown as first day of the month)
        @apiSuccess {Number}    datum.count How many profiles were created in that month
        """

        try:
            result = reports_profiles_by_month.get(start, end)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e)

        resp.status = falcon.HTTP_200
        resp.body = json.dumps(result, default=encoder)
