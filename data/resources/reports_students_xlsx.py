import os
import uuid
import falcon
import pyexcel

from data.models.reports_students_grid import reports_students_grid
from data.resources.utils.options_mixin import OptionMixin
from config.settings import config

class Resource(OptionMixin):

    def __init__(self):
        self.storage_path = config["storage"]["storage_path"] + "/reports"

    def on_get(self, req, resp):
        """
        @api {get} /reports/students.xlsx   Get data about student profiles and conversations, in Excel format
        @apiName GetStudentsReportExcel
        @apiGroup Reports

        @apiSuccess {File}  students.xlsx
        """

        # Create the filename for the temporary file
        reports_folder = self.storage_path + "/students/"
        if not os.path.exists(reports_folder):
            os.makedirs(reports_folder)
        filepath = reports_folder + str(uuid.uuid4()) + ".xlsx"

        # Get the data
        try:
            result = reports_students_grid.get()
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', e)

        data = result

        # Transform the data into XLSX and save to the temporary file
        sheet = pyexcel.get_sheet(records=data)
        sheet.save_as(filepath)

        # Serve the temporary file
        resp.stream = open(filepath, 'rb')
        resp.stream_len = os.path.getsize(filepath)
        resp.content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        # Delete the temporary file
        os.remove(filepath)
