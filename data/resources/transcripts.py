import falcon
import json

from data.resources.utils.options_mixin import OptionMixin
from config.settings import config
import os

# class Resource(object):
class Resource(OptionMixin):

    def __init__(self):
        self.storage_path = config["storage"]["storage_path"] + "/students"

    """
    @api {post} /transcripts Saves a new transcript
    @apiVersion 0.1.0
    @apiName NewTranscript
    @apiGroup Student
    """
    def on_post(self, req, resp, username):
        student_folder = self.storage_path +"/" + username + "/transcripts"

        transcript_file = req.get_param('transcript').file
        transcript_filename = req.get_param('transcript').filename
        save_path = os.path.join(student_folder +"/" + transcript_filename)

        try:
            if not os.path.exists(student_folder):
                os.makedirs(student_folder)
        except Exception:
            raise falcon.HTTPError(falcon.HTTP_500,
                                   'Storage Error',
                                   'Directory does not exist. <%s>' % self.storage_path)

        with open(save_path, 'wb') as save_file:
            while True:
                chunk = transcript_file.read(4096)
                if not chunk:
                    break

                save_file.write(chunk)

        resp.location = save_path

    """
    @api {get} /transcripts Lists the transcripts for a student
    @apiVersion 0.1.0
    @apiName ListTranscripts
    @apiGroup Student
    """
    def on_get(self, req, resp, username):
        student_folder = self.storage_path +"/" + username + "/transcripts"
        try:
            file_list = os.listdir(student_folder)
        except FileNotFoundError:
            file_list = []

        resp.body = json.dumps(file_list)
