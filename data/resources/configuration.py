import falcon
import json

from data.resources.utils.options_mixin import OptionMixin
from config.settings import Configuration


class Resource(OptionMixin):
    """
    @api {get} /configuration/ Get the configuration
    @apiVersion 0.1.0
    @apiGroup Configuration

    @apiSuccess {String} message .
    """

    def on_get(self, req, resp):
        # get the configuration data for the app
        cfg = Configuration()
        cfg.get_config()

        # TO DO : find a way to change it in the application

        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"message": "configuration update done"})
