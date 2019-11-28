import falcon
from data.resources.utils.options_mixin import OptionMixin
from config.settings import config
import os
import mimetypes

# class Resource(object):
class Resource(OptionMixin):

    def __init__(self):
        self.storage_path = config["storage"]["storage_path"] + "/students"

    """
    @api {get} /students/{username}/cvs/{filename} Shows a saved CV
    @apiVersion 0.1.0
    @apiName ReadCV
    @apiGroup Student
    """
    def on_get(self, req, resp, username, filename):
        filepath = self.storage_path + "/" + username + "/cvs/" + filename
        try:
            resp.stream = open(filepath, 'rb')
            resp.stream_len = os.path.getsize(filepath)
            resp.content_type = mimetypes.guess_type(filename)[0]
        except:
            resp.status = falcon.HTTP_404 # If no file, return FILE_NOT_FOUND

    """
    @api {delete} /students/{username}/cvs/{filename} Deletes a saved CV
    @apiVersion 0.1.0
    @apiName DeleteCV
    @apiGroup Student
    """
    def on_delete(self, req, resp, username, filename):
        filepath = self.storage_path + "/" + username + "/cvs/" + filename

        try:
            os.remove(filepath)
        except FileNotFoundError:
            pass # If the file doesn't exist, we don't worry about deleting it.
