import etcd
import json
import os


def set_dev():
    try:
        odin_dev = {
            "db": {
                'flavor': 'postgresql',
                'driver': 'psycopg2cffi',
                'user': 'odin',
                'pwd': 'y0uguysr0ck',
                'host': 'db',
                'db_name': 'midgard'
            },
            "cache": {
                'host': '10.0.2.15',
                'port': 6379
            },
            "wf": {
                'protocol':'http',
                'host': '10.0.2.15',
                'port': 5000
            },
            "storage":{
                'storage_path': '/usr/src/myapp/_documents'
            }
        }

        etcd_config = json.loads(os.environ['ETCD_ENV'])
        # client = etcd.Client(host='10.0.2.15', port=2379)
        client = etcd.Client(host=etcd_config['host'], port=etcd_config['port'])

        client.write('/envs/ODIN_DEV', json.dumps(odin_dev))
        # client.write('/envs/ODIN_STAGING', json.dumps(odin_dev))

        print(client.read('/envs/ODIN_DEV').value)

        r = client.read('/envs', recursive=True, sorted=True)
        for child in r.children:
            print("%s: %s" % (child.key, child.value))

    except Exception as e:
        print("Unable to set configuration")
        raise


def get_envs():
    try:
        etcd_config = json.loads(os.environ['ETCD_ENV'])
        client = etcd.Client(host=etcd_config['host'], port=etcd_config['port'])

        r = client.read('/envs', recursive=True, sorted=True)
        for child in r.children:
            print("%s: %s" % (child.key, child.value))

    except Exception as e:
        print("Unable to set configuration")
        raise


def set_test():
    try:
        odin_test = {
            "db": {
                'flavor1': 'postgresql',
                'driver': 'psycopg2cffi',
                'user': 'odin',
                'pwd': 'y0uguysr0ck',
                'host': '10.0.2.15',
                'db_name': 'midgard'
            },
            "cache": {
                'host': '10.0.2.15',
                'port': 6379
            }
        }

        client = etcd.Client(host='172.17.0.4', port=2379)
        client.write('/envs/ODIN_TEST', json.dumps(odin_test))

        print(client.read('/envs/ODIN_TEST').value)

        r = client.read('/envs', recursive=True, sorted=True)
        for child in r.children:
            print("%s: %s" % (child.key, child.value))

    except Exception as e:
        print("Unable to set configuration")
        raise

set_dev()
get_envs()
