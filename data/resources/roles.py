import falcon
import json
import requests

from data.models.student import student
from data.models.admin import admin
from data.resources.utils.alchemyencode import encoder
from data.resources.utils.options_mixin import OptionMixin
from config.settings import config


class Resource(OptionMixin):

	def on_get(self, req, resp, username):
		role = ""
		id = None
		
		# check if student
		try:
			# if the email doesn't have '@' then the username might be for an internal student. Therefore append '@uottawa' to compare with the email field in the students table
			studentEmail = username if '@' in username else username + '@uottawa.ca'
			result = student.get_by_email(studentEmail)
		except Exception as e:
			raise falcon.HTTPError(falcon.HTTP_400, 'Database Error', 'DB exception: %s' % e)
		if result is not None:
			role = "student"
			id = result['id']

		# Only external students have '@' in their username. For this group, if they don't exist in students table there is no need to check further 
		elif '@' in username:
  			pass

		else:
			# check if admin
			try:
				result = admin.get_by_username(username)
			except Exception as e:
				raise falcon.HTTPError(falcon.HTTP_400, 'Database Error', 'DB exception: %s' % e)
			if result is not None:
				role = "admin"
				id = result['id']

			else:
				# check if Prof
				result = requests.get(config["UNIWeb"]["host"] + '/professors/' + username) # verify=False # TODO remove verify=False on Production
				jsonResult = json.loads(result.content.decode('utf-8'))
				if jsonResult and 'id' in jsonResult:
					role = "researcher"
					id = jsonResult['id']


		resp.status = falcon.HTTP_200
		resp.body = json.dumps({ "role": role, "id": id })