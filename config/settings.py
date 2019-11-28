"""
This module provides configuration to all of the other modules in this application.

In it's current state, it uses the envs variable, but the goal is to retrieve configuration
information from etcd.

"""
# import etcd
# from etcd.client import Client
# import json
# import os
# from cerberus import Validator, errors
# from data.resources.schemas.configuration import schema_config
# from collections import defaultdict

config = {
            "db": {
                'flavor': 'postgresql',
                'driver': 'psycopg2cffi',
                'user': 'odin',
                'pwd': 'y0uguysr0ck',
                'host': 'db',
                'db_name': 'midgard'
            },
            "cache": {
                'host': 'redis',
                'port': 6379
            },
            "wf": {
                'protocol':'http',
                'host': '10.0.2.15',
                'port': 5000
            },
            "storage":{
                'storage_path': '/usr/src/tmp_fu'
            },
            "UNIWeb": {
                "host": 'https://uniweb-service.med.uottawa.ca' # lcoal 10.0.2.15:5005 # TODO: put back on Prod --> 'https://uniweb-service.med.uottawa.ca'
            },
            "email": {
                # "server_addr": "https://api.sendinblue.com/v2.0",
                "server_addr": "relay.csmtp.net",
                # "server_addr": "smtp-relay.csmtp.net",
                # "API_Key": 'XF7YaPKrMWqQ604f',
                'username':'kshapiro@uottawa.ca', # TODO: update to use same credentials as other apps--but without storing the password in Git
                'password':'0Yv482I^670U',
                'port':'587',
                "report_group": "7508",
                "from_addr": "tss-rdt@uottawa.ca",
                "tss_admin_addrs": "Louise.Lemay@uottawa.ca", # TODO: put back on Prod --> # Louise.Lemay@uottawa.ca
                "front_end_address": "https://tss.med.uottawa.ca/"
            }
}

# 10.80.128.44

def get_db_url():
    db_env = config['db']

    return '{0}+{1}://{2}:{3}@{4}/{5}' \
        .format(db_env['flavor'],
                db_env['driver'],
                db_env['user'],
                db_env['pwd'],
                db_env['host'],
                db_env['db_name'])



