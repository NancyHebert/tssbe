define({ "api": [
  {
    "type": "delete",
    "url": "/organizations/:organization_id",
    "title": "Remove a organization",
    "version": "0.1.0",
    "name": "DELETE__organizations__id",
    "group": "organization",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organization.py",
    "groupTitle": "organization"
  },
  {
    "type": "get",
    "url": "/organizations",
    "title": "Find all organizations",
    "version": "0.1.0",
    "name": "GET__organizations",
    "group": "organization",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Organization ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organizations.py",
    "groupTitle": "organization"
  },
  {
    "type": "get",
    "url": "/organizations/:organization_id",
    "title": "Find a organization",
    "version": "0.1.0",
    "name": "GET__organizations__id",
    "group": "organization",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The organization ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organization.py",
    "groupTitle": "organization"
  },
  {
    "type": "post",
    "url": "/organization/:organization_id",
    "title": "Add a organization",
    "version": "0.1.0",
    "name": "POST__organizations",
    "group": "organization",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Organization ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organizations.py",
    "groupTitle": "organization"
  },
  {
    "type": "update",
    "url": "/organizations/:organization_id",
    "title": "Update a organization",
    "version": "0.1.0",
    "name": "UPDATE__organizations__id",
    "group": "organization",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organization.py",
    "groupTitle": "organization"
  },
  {
    "type": "get",
    "url": "/organizations/:organization_id/people/types",
    "title": "Find all people types in organization",
    "version": "0.1.0",
    "name": "GET__organizations__id_people_types",
    "group": "organization_person_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organization_person_types.py",
    "groupTitle": "organization_person_type"
  },
  {
    "type": "post",
    "url": "/organizations/:organization_id/people/types",
    "title": "Add person type to a organization",
    "version": "0.1.0",
    "name": "POST__organizations__id_people_types",
    "group": "organization_person_type",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organization_person_types.py",
    "groupTitle": "organization_person_type"
  },
  {
    "type": "delete",
    "url": "/organizations/:organization_id/people/types/:person_type_id",
    "title": "Delete One Person Type in Organization",
    "version": "0.1.0",
    "name": "DELETE__organizations__id_people_types__id",
    "group": "organization_person_types",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organization_person_type.py",
    "groupTitle": "organization_person_types"
  },
  {
    "type": "get",
    "url": "/organizations/:organization_id/people/types/:person_type_id",
    "title": "Find One Person Type in Organization",
    "version": "0.1.0",
    "name": "GET__organizations__id_people_types__id",
    "group": "organization_person_types",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organization_person_type.py",
    "groupTitle": "organization_person_types"
  },
  {
    "type": "update",
    "url": "/organizations/:organization_id/people/types/:person_type_id",
    "title": "Update One Person Type in Organization",
    "version": "0.1.0",
    "name": "UPDATE__organizations__id_people_types__id",
    "group": "organization_person_types",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organization_person_type.py",
    "groupTitle": "organization_person_types"
  },
  {
    "type": "get",
    "url": "/organization/:organization_id/types",
    "title": "Find all organization type",
    "version": "0.1.0",
    "name": "GET__organization__id_types",
    "group": "organization_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Organization ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organization_types.py",
    "groupTitle": "organization_type"
  },
  {
    "type": "post",
    "url": "/organization/:organization_id/types",
    "title": "Add a organization type",
    "version": "0.1.0",
    "name": "POST__organization__id_types",
    "group": "organization_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "organization_id",
            "description": "<p>The Organization ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Organization ID.</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/organization_types.py",
    "groupTitle": "organization_type"
  },
  {
    "type": "get",
    "url": "/people",
    "title": "Find all people",
    "version": "0.1.0",
    "name": "GET__people",
    "group": "people",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Person ID</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>The person first name</p>"
          },
          {
            "group": "Success 200",
            "type": "string",
            "optional": false,
            "field": "middle_initial",
            "description": "<p>The person middle initial</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>The person last name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "date_of_birth",
            "description": "<p>The person DOB</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/people.py",
    "groupTitle": "people"
  },
  {
    "type": "post",
    "url": "/people",
    "title": "Add a person",
    "version": "0.1.0",
    "name": "POST__people",
    "group": "people",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Person ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/people.py",
    "groupTitle": "people"
  },
  {
    "type": "delete",
    "url": "/people/:person_id",
    "title": "Remove a person",
    "version": "0.1.0",
    "name": "DELETE__people__id",
    "group": "person",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_id",
            "description": "<p>The Person ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person.py",
    "groupTitle": "person"
  },
  {
    "type": "get",
    "url": "/people/:person_id",
    "title": "Find a person",
    "version": "0.1.0",
    "name": "GET__people__id",
    "group": "person",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_id",
            "description": "<p>people unique ID.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Person ID</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>The Person first name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>The Person last name</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person.py",
    "groupTitle": "person"
  },
  {
    "type": "patch",
    "url": "/people/:person_id",
    "title": "Update a person",
    "version": "0.1.0",
    "name": "UPDATE__people__id",
    "group": "person",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_id",
            "description": "<p>The Person ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person.py",
    "groupTitle": "person"
  },
  {
    "type": "delete",
    "url": "/people/:person_id/types/:type_id",
    "title": "Remove a person type",
    "version": "0.1.0",
    "name": "DELETE__people__id_types__id",
    "group": "person_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_id",
            "description": "<p>The Person ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person_type.py",
    "groupTitle": "person_type"
  },
  {
    "type": "get",
    "url": "/people/:person_id/types",
    "title": "Find all person type",
    "version": "0.1.0",
    "name": "GET__people__id_types",
    "group": "person_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_id",
            "description": "<p>The Person ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person_types.py",
    "groupTitle": "person_type"
  },
  {
    "type": "get",
    "url": "/people/:person_id/types/:person_type_id",
    "title": "Find a person type",
    "version": "0.1.0",
    "name": "GET__people__id_types__id",
    "group": "person_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_id",
            "description": "<p>The Person ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Type ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person_type.py",
    "groupTitle": "person_type"
  },
  {
    "type": "post",
    "url": "/people/:person_id/types",
    "title": "Add a person type",
    "version": "0.1.0",
    "name": "POST__people__id_types",
    "group": "person_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_id",
            "description": "<p>The Person ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person_types.py",
    "groupTitle": "person_type"
  },
  {
    "type": "patch",
    "url": "/people/:person_id/types/:type_id",
    "title": "Update a person type",
    "version": "0.1.0",
    "name": "UPDATE__people__id_types_id",
    "group": "person_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_id",
            "description": "<p>The Person ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person_type.py",
    "groupTitle": "person_type"
  },
  {
    "type": "delete",
    "url": "/people/types/:person_type_id/programs/:program_id",
    "title": "Delete a program under people types",
    "version": "0.1.0",
    "name": "DELETE__people_types__id_programs__id",
    "group": "person_type_program",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person_type_program.py",
    "groupTitle": "person_type_program"
  },
  {
    "type": "get",
    "url": "/people/types/:person_type_id/programs",
    "title": "Find all program under people types",
    "version": "0.1.0",
    "name": "GET__people_types__id_programs",
    "group": "person_type_program",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person_type_programs.py",
    "groupTitle": "person_type_program"
  },
  {
    "type": "get",
    "url": "/people/types/:person_type_id/programs",
    "title": "Add a program under people types",
    "version": "0.1.0",
    "name": "GET__people_types__id_programs",
    "group": "person_type_program",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person_type_programs.py",
    "groupTitle": "person_type_program"
  },
  {
    "type": "get",
    "url": "/people/types/:person_type_id/programs/:program_id",
    "title": "Find a program under people types",
    "version": "0.1.0",
    "name": "GET__people_types__id_programs__id",
    "group": "person_type_program",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person_type_program.py",
    "groupTitle": "person_type_program"
  },
  {
    "type": "update",
    "url": "/people/types/:person_type_id/programs/:program_id",
    "title": "Update a program under people types",
    "version": "0.1.0",
    "name": "UPDATE__people_types__id_programs__id",
    "group": "person_type_program",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_type_id",
            "description": "<p>The Person_Type ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/person_type_program.py",
    "groupTitle": "person_type_program"
  },
  {
    "type": "delete",
    "url": "/programs/:program_id",
    "title": "Find a program",
    "version": "0.1.0",
    "name": "DELETE__programs__id",
    "group": "program",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/program.py",
    "groupTitle": "program"
  },
  {
    "type": "get",
    "url": "/programs",
    "title": "Find all program",
    "version": "0.1.0",
    "name": "GET__programs",
    "group": "program",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/programs.py",
    "groupTitle": "program"
  },
  {
    "type": "get",
    "url": "/programs/:program_id",
    "title": "Find a program",
    "version": "0.1.0",
    "name": "GET__programs__id",
    "group": "program",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/program.py",
    "groupTitle": "program"
  },
  {
    "type": "post",
    "url": "/programs",
    "title": "Add a program",
    "version": "0.1.0",
    "name": "POST__programs",
    "group": "program",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/programs.py",
    "groupTitle": "program"
  },
  {
    "type": "update",
    "url": "/programs/:program_id",
    "title": "Update a program",
    "version": "0.1.0",
    "name": "UPDATE__programs__id",
    "group": "program",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/program.py",
    "groupTitle": "program"
  },
  {
    "type": "delete",
    "url": "/programs/:program_id/Types/:program_type_id",
    "title": "Delete a program type",
    "version": "0.1.0",
    "name": "DELETE__programs__id_Types__id",
    "group": "program_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_type_id",
            "description": "<p>The Program_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/program_type.py",
    "groupTitle": "program_type"
  },
  {
    "type": "get",
    "url": "/programs/:program_id/Types",
    "title": "Find all program type",
    "version": "0.1.0",
    "name": "GET__programs__id_Types",
    "group": "program_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Program_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/program_types.py",
    "groupTitle": "program_type"
  },
  {
    "type": "get",
    "url": "/programs/:program_id/Types/:program_type_id",
    "title": "Find a program type",
    "version": "0.1.0",
    "name": "GET__programs__id_Types__id",
    "group": "program_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_type_id",
            "description": "<p>The Program_Type ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Program_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/program_type.py",
    "groupTitle": "program_type"
  },
  {
    "type": "post",
    "url": "/programs/:program_id/Types",
    "title": "Add a program type",
    "version": "0.1.0",
    "name": "POST__programs__id_Types",
    "group": "program_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Program_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/program_types.py",
    "groupTitle": "program_type"
  },
  {
    "type": "update",
    "url": "/programs/:program_id/Types/:program_type_id",
    "title": "Update a program type",
    "version": "0.1.0",
    "name": "Update__programs__id_Types__id",
    "group": "program_type",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_id",
            "description": "<p>The Program ID</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_type_id",
            "description": "<p>The Program_Type ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/program_type.py",
    "groupTitle": "program_type"
  },
  {
    "type": "delete",
    "url": "/researcher/profiles/:researcher_profile_id",
    "title": "Delete a researcher profile",
    "version": "0.1.0",
    "name": "DELETE__researcher_profiles__researcher_profile_id",
    "group": "researcher_profile",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "researcher_profile_id",
            "description": "<p>The Researcher_Profile ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/researcher_profile.py",
    "groupTitle": "researcher_profile"
  },
  {
    "type": "get",
    "url": "/researcher/profiles",
    "title": "Find all researcher profile",
    "version": "0.1.0",
    "name": "GET__researcher_profiles",
    "group": "researcher_profile",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Researcher_Profile ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/researcher_profiles.py",
    "groupTitle": "researcher_profile"
  },
  {
    "type": "get",
    "url": "/researcher/profiles/:researcher_profile_id",
    "title": "Find a researcher profile",
    "version": "0.1.0",
    "name": "GET__researcher_profiles__researcher_profile_id",
    "group": "researcher_profile",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "researcher_profile_id",
            "description": "<p>The Researcher_Profile ID</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Researcher_Profile ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/researcher_profile.py",
    "groupTitle": "researcher_profile"
  },
  {
    "type": "post",
    "url": "/researcher/profiles",
    "title": "add a researcher profile",
    "version": "0.1.0",
    "name": "POST__researcher_profiles",
    "group": "researcher_profile",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Researcher_Profile ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/researcher_profiles.py",
    "groupTitle": "researcher_profile"
  },
  {
    "type": "update",
    "url": "/researcher/profiles/:researcher_profile_id",
    "title": "Update a researcher profile",
    "version": "0.1.0",
    "name": "UPDATE__researcher_profiles__researcher_profile_id",
    "group": "researcher_profile",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "researcher_profile_id",
            "description": "<p>The Researcher_Profile ID</p>"
          }
        ]
      }
    },
    "filename": "./data/resources/researcher_profile.py",
    "groupTitle": "researcher_profile"
  }
] });
