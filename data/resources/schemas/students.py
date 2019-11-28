schema_post = {
    'username': {
        'required': True,
        'type': 'string'
    },
    'name': {
        'required': True,
        'type': 'string'
    },
    'email': {
        'required': True,
        'type': 'string',
        'regex': '.*@.*'
    },
    'program_code': {
        'type': 'integer'
    },
    'admitted': {
        'type': 'string'
    },
    'level_of_instruction': {
        'type': 'string',
        'maxlength': 3
    }
}
