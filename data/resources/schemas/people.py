schema_post = {
    'first_name': {
        'type': 'string',
        'required': True,
        'empty': False,
        'maxlength': 50
    },
    'middle_name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1
    },
    'last_name': {
        'type': 'string',
        'required': True,
        'empty': False,
        'maxlength': 50
    },
    'date_of_birth': {
        'type': 'integer'
    },
    'person_types_id': {
        'type': 'integer',
        'required': True
    }
}

schema_update = {
    'first_name': {
        'type': 'string',
        'empty': False,
        'maxlength': 50
    },
    'middle_name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1
    },
    'last_name': {
        'type': 'string',
        'empty': False,
        'maxlength': 50
    },
    'date_of_birth': {
        'type': 'integer'
    },
    'person_types_id': {
        'type': 'integer'
    }
}
