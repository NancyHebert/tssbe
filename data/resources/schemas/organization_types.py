schema_post = {
    'is_active': {
        'type': 'boolean'
    },
    'organization_type_names': {
        'type': 'list', 'schema': {
            'type': 'dict', 'schema': {
                'lang': {
                    'type': 'string',
                    'required': True,
                    'empty': False,
                    'minlength': 2,
                    'maxlength': 2
                },
                'name': {
                    'type': 'string',
                    'required': True,
                    'empty': False,
                    'maxlength': 50
                }
            }
        }
    }
}

schema_update = {
    'is_active': {
        'type': 'boolean'
    },
    'organization_type_names': {
        'type': 'list', 'schema': {
            'type': 'dict', 'schema': {
                'lang': {
                    'type': 'string',
                    'required': True,
                    'empty': False,
                    'minlength': 2,
                    'maxlength': 2
                },
                'name': {
                    'type': 'string',
                    'empty': False,
                    'maxlength': 50
                }
            }
        }
    }
}
