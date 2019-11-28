schema_post = {
    'parent_id': {
        'type': 'integer'
    },
    'organization_types_id': {
        'type': 'integer', 
        'required': True
    },
    'is_active': {
        'type': 'boolean'
    },
    'organization_names': {
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
                },
                'full_path': {
                    'required': True,
                    'type': 'string',
                    'empty': False,
                }
            }
        }
    }
}

schema_update = {
    'parent_id': {
        'type': 'integer'
    },
    'organization_types_id': {
        'type': 'integer'
    },
    'is_active': {
        'type': 'boolean'
    },
    'organization_names': {
        'type': 'list', 'schema': {
            'type': 'dict', 'schema': {
                'lang': {
                    'type': 'string', 
                    'empty': False, 
                    'minlength': 2, 
                    'maxlength': 2
                },
                'name': {
                    'type': 'string', 
                    'empty': False, 
                    'maxlength': 50
                },
                'full_path': {
                    'type': 'string',
                    'empty': False
                }
            }
        }
    }
}
