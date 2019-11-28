schema_update = {
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
