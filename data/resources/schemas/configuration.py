schema_config = {
    'db': {
        'type': 'dict', 'schema': {
            'flavor': {
                'type': 'string',
                'required': True
            },
            'driver': {
                'type': 'string',
                'required': True
            },
            'user': {
                'type': 'string',
                'required': True
            },
            'pwd': {
                'type': 'string',
                'required': True
            },
            'host': {
                'type': 'string',
                'required': True
            },
            'db_name': {
                'type': 'string',
                'required': True
            }
        }
    },
    'cache': {
        'type': 'dict', 'schema': {
            'host': {
                'type': 'string',
                'required': True
            },
            'port': {
                'type': 'string',
                'required': True
            }
        }
    },
    'wf': {
        'type': 'dict', 'schema': {
            'protocol': {
                'type': 'string',
                'required': True
            },
            'host': {
                'type': 'string',
                'required': True
            },
            'port': {
                'type': 'string',
                'required': True
            }
        }
    },
    'storage': {
        'type': 'dict', 'schema': {
            'storage_path': {
                'type': 'string',
                'required': True
            }
        }
    },
    'environment': {
        'type': 'dict', 'schema': {
             'environment_name': {
                'type': 'string',
                'required': True
              }, 
              'service_name': {
                'type': 'string',
                'required': True
              },
              'domain_name': {
                'type': 'string',
                'required': True
              },
              'service_subdomain': {
                'type': 'string',
                'required': True
              },
              'host_ip': {
                'type': 'string',
                'required': True
              },
              'ext_port': {
                'type': 'string',
                'required': True
              },
              'int_port': {
                'type': 'string',
                'required': True
              },
              'etcd_environment': {
                'type': 'string',
                'required': True
              }
        }
    }


}
  