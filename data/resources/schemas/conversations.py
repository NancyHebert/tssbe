schema_post = {
    'researcher_uniweb_number': {
        'required': True,
        'type': 'integer'
    },

    'researcher_name': {
        'type': 'string'
    },

    'student_username': {
        'required': True,
        'type': 'string'
    },

    'student_name': {
        'type': 'string'
    },

    'body': {
        'required': True,
        'type': 'string',
        'empty': False
    },
    'is_from_student': {
        'required': True,
        'type': 'boolean'
    },
    'is_draft': {
        'required': True,
        'type': 'boolean'
    },
    'level_of_instruction_en': {
        'type': 'string'
    },

    'level_of_instruction_fr': {
        'type': 'string'
    },

    'admitted_en': {
        'type': 'string'
    },

    'admitted_fr': {
        'type': 'string'
    },

    'program_code_en': {
        'type': 'string'
    },

    'program_code_fr': {
        'type': 'string'
    }
}
