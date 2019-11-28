"""
The functionnalities of this module are :

1. to register with the workflow engine
2. to schedule emails with the workflow engine  

"""
import json
import requests

from config.settings import Configuration
from data.models.security_token import security_token

class workflow:
    def __init__(self):
        # get the configuration for the workflow engine
         cfg = Configuration()
         config = cfg.get_config()
         self.wf_congig = config["wf"]
         self.wf_url_prefix = "{}://{}:{}".format(self.wf_congig["protocol"],self.wf_congig["host"],self.wf_congig["port"])

    def register(self):
        #register with workflow engine, get token
        data = { "appName" : "Odin" }
        r = requests.post(self.wf_url_prefix + "/register",json=data)

        if r.status_code != requests.codes.ok:
            raise r.raise_for_status()

        try:            
            #token
            result = r.json()
            token_json = {"token":result["token"], "app_name" : "workflow", "host" : r.request.url}
        except Exception as e:
            raise ErrorMessage('Invalid JSON', 'Invalid JSON : %s' % e)

        try:
            #save token in the database
            t = security_token.post(token_json)
            return result["token"]
        except Exception as e:
            raise ErrorMessage('Database Error', 'Unable to save token : %s' % e)

    def send_email(self, afrom, ato, subject, message, send_date):
        try:
            #get token to be added in the header
            result = security_token.get('workflow').first()

            if result:
                token = result["token"]
            else:
                token = self.register()

            data = {
                    "sendDate" : send_date,
                    "email" : { "from" : afrom, 
                                "to": ato, 
                                "subject" : subject, 
                                "message" : message 
                              }
                    }

            # send email by the use of the workflow engine
            url = self.wf_url_prefix + "/reminder"
            headers = {'content-type': 'application/json', 'Securitytoken': token}

            r = requests.post(url,json=data, headers=headers)

            if r.status_code != requests.codes.ok:
               raise r.raise_for_status()

        except Exception as e:
            raise ErrorMessage('ErrorEmail', 'Unable to send email: %s' % e)

# Custom errors

class Error(Exception):
    pass


class ErrorMessage(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message