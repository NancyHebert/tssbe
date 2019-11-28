define({ "api": [
  {
    "type": "delete",
    "url": "/organizations/:organization_id/people/types/:person_type_id",
    "title": "Delete a person type in organization",
    "version": "0.1.0",
    "name": "DELETE__organizations__id_people_types__id",
    "group": "Organization_Person_Types",
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
    "filename": "../odin/data/resources/organization_person_type.py",
    "groupTitle": "Organization_Person_Types"
  },
  {
    "type": "get",
    "url": "/organizations/:organization_id/people/types",
    "title": "Find all people types in organization",
    "version": "0.1.0",
    "name": "GET__organizations__id_people_types",
    "group": "Organization_Person_Types",
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
    "filename": "../odin/data/resources/organization_person_types.py",
    "groupTitle": "Organization_Person_Types"
  },
  {
    "type": "get",
    "url": "/organizations/:organization_id/people/types/:person_type_id",
    "title": "Get a person type in organization",
    "version": "0.1.0",
    "name": "GET__organizations__id_people_types__id",
    "group": "Organization_Person_Types",
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
    "filename": "../odin/data/resources/organization_person_type.py",
    "groupTitle": "Organization_Person_Types"
  },
  {
    "type": "post",
    "url": "/organizations/:organization_id/people/types",
    "title": "Create a person type in organization",
    "version": "0.1.0",
    "name": "POST__organizations__id_people_types",
    "group": "Organization_Person_Types",
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
    "filename": "../odin/data/resources/organization_person_types.py",
    "groupTitle": "Organization_Person_Types"
  },
  {
    "type": "update",
    "url": "/organizations/:organization_id/people/types/:person_type_id",
    "title": "Update a person type in organization",
    "version": "0.1.0",
    "name": "UPDATE__organizations__id_people_types__id",
    "group": "Organization_Person_Types",
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
    "filename": "../odin/data/resources/organization_person_type.py",
    "groupTitle": "Organization_Person_Types"
  },
  {
    "type": "delete",
    "url": "/organizationTypes/:organization_types_id",
    "title": "Delete a organization types",
    "version": "0.1.0",
    "name": "DELETE__organizationTypes__organization_types_id",
    "group": "Organization_Types",
    "filename": "../odin/data/resources/organization_type.py",
    "groupTitle": "Organization_Types"
  },
  {
    "type": "get",
    "url": "/organizationTypes/:organization_types_id",
    "title": "Get a organization types",
    "version": "0.1.0",
    "name": "GET__organizationTypes__organization_types_id",
    "group": "Organization_Types",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Organization Types ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/organization_type.py",
    "groupTitle": "Organization_Types"
  },
  {
    "type": "get",
    "url": "/organizationTypes/:organization_types_id",
    "title": "Get all organization types",
    "version": "0.1.0",
    "name": "GET__organizationTypes__organization_types_id",
    "group": "Organization_Types",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Organization Types ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/organization_types.py",
    "groupTitle": "Organization_Types"
  },
  {
    "type": "post",
    "url": "/organizationTypes/:organization_types_id",
    "title": "Create a organization types",
    "version": "0.1.0",
    "name": "POST__organizationTypes__organization_types_id",
    "group": "Organization_Types",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "organization_type_names",
            "description": "<p>Organization_type_names information.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "2..2",
            "optional": false,
            "field": "organization_type_names.lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": false,
            "field": "organization_type_names.name",
            "description": "<p>The name.</p>"
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
            "description": "<p>The organization_types ID.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/organization_types.py",
    "groupTitle": "Organization_Types"
  },
  {
    "type": "update",
    "url": "/organizationTypes/:organization_types_id",
    "title": "Update a organization types",
    "version": "0.1.0",
    "name": "UPDATE__organizationTypes__organization_types_id",
    "group": "Organization_Types",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "organization_type_names",
            "description": "<p>Organization_type_names information.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "2..2",
            "optional": true,
            "field": "organization_type_names.lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": true,
            "field": "organization_type_names.name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/organization_type.py",
    "groupTitle": "Organization_Types"
  },
  {
    "type": "delete",
    "url": "/organizations/:organizations_id",
    "title": "Delete a organization",
    "version": "0.1.0",
    "name": "DELETE__organizations__organizations_id",
    "group": "Organizations",
    "filename": "../odin/data/resources/organization.py",
    "groupTitle": "Organizations"
  },
  {
    "type": "get",
    "url": "/organizations",
    "title": "Get all organizations",
    "version": "0.1.0",
    "name": "GET__organizations",
    "group": "Organizations",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The organization ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "parent_id",
            "description": "<p>The parent_id.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "organization_types_id",
            "description": "<p>The organization_type.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "full_path",
            "description": "<p>The full path.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/organizations.py",
    "groupTitle": "Organizations"
  },
  {
    "type": "get",
    "url": "/organizations/:organizations_id",
    "title": "Get a organization",
    "version": "0.1.0",
    "name": "GET__organizations__organizations_id",
    "group": "Organizations",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The organization ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "parent_id",
            "description": "<p>The parent_id.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "organization_types_id",
            "description": "<p>The organization_type.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "full_path",
            "description": "<p>The full path.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/organization.py",
    "groupTitle": "Organizations"
  },
  {
    "type": "post",
    "url": "/organizations",
    "title": "Create a organization",
    "version": "0.1.0",
    "name": "POST__organizations",
    "group": "Organizations",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "parent_id",
            "description": "<p>The parent_id.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "organization_types_id",
            "description": "<p>The organization_type.</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "organization_names",
            "description": "<p>Organization_names information.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "2..2",
            "optional": false,
            "field": "organization_names.lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": false,
            "field": "organization_names.name",
            "description": "<p>The name.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "organization_names.full_path",
            "description": "<p>The full path.</p>"
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
    "filename": "../odin/data/resources/organizations.py",
    "groupTitle": "Organizations"
  },
  {
    "type": "update",
    "url": "/organizations/:organizations_id",
    "title": "Update a organization",
    "version": "0.1.0",
    "name": "UPDATE__organizations__organizations_id",
    "group": "Organizations",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "parent_id",
            "description": "<p>The parent_id.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "organization_types_id",
            "description": "<p>The organization_type.</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "organization_names",
            "description": "<p>Organization_names information.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "2..2",
            "optional": true,
            "field": "organization_names.lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": true,
            "field": "organization_names.name",
            "description": "<p>The name.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "organization_names.full_path",
            "description": "<p>The full path.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/organization.py",
    "groupTitle": "Organizations"
  },
  {
    "type": "delete",
    "url": "/people/:people_id",
    "title": "Delete a person",
    "version": "0.1.0",
    "name": "DELETE__people__people_id",
    "group": "People",
    "filename": "../odin/data/resources/person.py",
    "groupTitle": "People"
  },
  {
    "type": "get",
    "url": "/people",
    "title": "Get all people",
    "version": "0.1.0",
    "name": "GET__people",
    "group": "People",
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
            "description": "<p>First name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "middle_initial",
            "description": "<p>Middle initial.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>Last name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Date",
            "optional": false,
            "field": "date_of_birth",
            "description": "<p>Date of birth.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "person_types_id",
            "description": "<p>Person type id</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/people.py",
    "groupTitle": "People"
  },
  {
    "type": "get",
    "url": "/people/:people_id",
    "title": "Get a person",
    "version": "0.1.0",
    "name": "GET__people__people_id",
    "group": "People",
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
            "description": "<p>First name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "middle_initial",
            "description": "<p>Middle initial.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>Last name.</p>"
          },
          {
            "group": "Success 200",
            "type": "Date",
            "optional": false,
            "field": "date_of_birth",
            "description": "<p>Date of birth.</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "person_types_id",
            "description": "<p>Person type id</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/person.py",
    "groupTitle": "People"
  },
  {
    "type": "post",
    "url": "/people",
    "title": "Create a person",
    "version": "0.1.0",
    "name": "POST__people",
    "group": "People",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": false,
            "field": "first_name",
            "description": "<p>First name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "1..1",
            "optional": true,
            "field": "middle_initial",
            "description": "<p>Middle initial.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": false,
            "field": "last_name",
            "description": "<p>Last name.</p>"
          },
          {
            "group": "Parameter",
            "type": "Date",
            "optional": false,
            "field": "date_of_birth",
            "description": "<p>Date of birth.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "person_types_id",
            "description": "<p>Person type id</p>"
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
          }
        ]
      }
    },
    "filename": "../odin/data/resources/people.py",
    "groupTitle": "People"
  },
  {
    "type": "update",
    "url": "/people/:people_id",
    "title": "Update a person",
    "version": "0.1.0",
    "name": "UPDATE__people__people_id",
    "group": "People",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": true,
            "field": "first_name",
            "description": "<p>First name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "1..1",
            "optional": true,
            "field": "middle_initial",
            "description": "<p>Middle initial.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": true,
            "field": "last_name",
            "description": "<p>Last name.</p>"
          },
          {
            "group": "Parameter",
            "type": "Date",
            "optional": true,
            "field": "date_of_birth",
            "description": "<p>Date of birth.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "person_types_id",
            "description": "<p>Person type id</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/person.py",
    "groupTitle": "People"
  },
  {
    "type": "delete",
    "url": "/people/types/:person_type_id/programs/:program_id",
    "title": "Delete a program under people types",
    "version": "0.1.0",
    "name": "DELETE__people_types__id_programs__id",
    "group": "Person_Type_Programs",
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
    "filename": "../odin/data/resources/person_type_program.py",
    "groupTitle": "Person_Type_Programs"
  },
  {
    "type": "get",
    "url": "/people/types/:person_type_id/programs",
    "title": "Get all program under people types",
    "version": "0.1.0",
    "name": "GET__people_types__id_programs",
    "group": "Person_Type_Programs",
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
    "filename": "../odin/data/resources/person_type_programs.py",
    "groupTitle": "Person_Type_Programs"
  },
  {
    "type": "get",
    "url": "/people/types/:person_type_id/programs",
    "title": "Create a program under people type",
    "version": "0.1.0",
    "name": "GET__people_types__id_programs",
    "group": "Person_Type_Programs",
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
    "filename": "../odin/data/resources/person_type_programs.py",
    "groupTitle": "Person_Type_Programs"
  },
  {
    "type": "get",
    "url": "/people/types/:person_type_id/programs/:program_id",
    "title": "Get a program under people types",
    "version": "0.1.0",
    "name": "GET__people_types__id_programs__id",
    "group": "Person_Type_Programs",
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
    "filename": "../odin/data/resources/person_type_program.py",
    "groupTitle": "Person_Type_Programs"
  },
  {
    "type": "update",
    "url": "/people/types/:person_type_id/programs/:program_id",
    "title": "Update a program under people types",
    "version": "0.1.0",
    "name": "UPDATE__people_types__id_programs__id",
    "group": "Person_Type_Programs",
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
    "filename": "../odin/data/resources/person_type_program.py",
    "groupTitle": "Person_Type_Programs"
  },
  {
    "type": "delete",
    "url": "/peopleTypes/:person_types_id",
    "title": "Delete a person type",
    "version": "0.1.0",
    "name": "DELETE__peopleTypes__person_types_id",
    "group": "Person_Types",
    "filename": "../odin/data/resources/person_type.py",
    "groupTitle": "Person_Types"
  },
  {
    "type": "get",
    "url": "/peopleTypes",
    "title": "Get all person types",
    "version": "0.1.0",
    "name": "GET__peopleTypes",
    "group": "Person_Types",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Person_Type ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "parent_id",
            "description": "<p>The parent id.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/person_types.py",
    "groupTitle": "Person_Types"
  },
  {
    "type": "get",
    "url": "/peopleTypes/:person_types_id",
    "title": "Get a person type",
    "version": "0.1.0",
    "name": "GET__peopleTypes__person_types_id",
    "group": "Person_Types",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The Person_Type ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "parent_id",
            "description": "<p>The parent id.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/person_type.py",
    "groupTitle": "Person_Types"
  },
  {
    "type": "post",
    "url": "/peopleTypes",
    "title": "Create a person type",
    "version": "0.1.0",
    "name": "POST__peopleTypes",
    "group": "Person_Types",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "parent_id",
            "description": "<p>The parent id.</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "person_type_names",
            "description": "<p>Person_type_names information.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "2..2",
            "optional": false,
            "field": "person_type_names.lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": false,
            "field": "person_type_names.name",
            "description": "<p>The name.</p>"
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
    "filename": "../odin/data/resources/person_types.py",
    "groupTitle": "Person_Types"
  },
  {
    "type": "update",
    "url": "/peopleTypes/:person_types_id",
    "title": "Update a person type",
    "version": "0.1.0",
    "name": "UPDATE__peopleTypes__person_types_id",
    "group": "Person_Types",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "parent_id",
            "description": "<p>The parent id.</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "person_type_names",
            "description": "<p>Person_type_names information.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "2..2",
            "optional": true,
            "field": "person_type_names.lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": true,
            "field": "person_type_names.name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/person_type.py",
    "groupTitle": "Person_Types"
  },
  {
    "type": "delete",
    "url": "/programsTypes/:program_types_id",
    "title": "Delete a program type",
    "version": "0.1.0",
    "name": "DELETE__programsTypes__program_types_id",
    "group": "Program_Types",
    "filename": "../odin/data/resources/program_type.py",
    "groupTitle": "Program_Types"
  },
  {
    "type": "get",
    "url": "/programTypes",
    "title": "Get all program types",
    "version": "0.1.0",
    "name": "GET__programsTypes",
    "group": "Program_Types",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The program type ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/program_types.py",
    "groupTitle": "Program_Types"
  },
  {
    "type": "get",
    "url": "/programsTypes/:program_types_id",
    "title": "Get a program type",
    "version": "0.1.0",
    "name": "GET__programsTypes__program_types_id",
    "group": "Program_Types",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The program type ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/program_type.py",
    "groupTitle": "Program_Types"
  },
  {
    "type": "post",
    "url": "/programsTypes",
    "title": "Create a program type",
    "version": "0.1.0",
    "name": "POST__programsTypes",
    "group": "Program_Types",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "program_type_names",
            "description": "<p>Program_type_names information.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "2..2",
            "optional": false,
            "field": "program_type_names.lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": false,
            "field": "program_type_names.name",
            "description": "<p>The name.</p>"
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
    "filename": "../odin/data/resources/program_types.py",
    "groupTitle": "Program_Types"
  },
  {
    "type": "update",
    "url": "/programsTypes/:program_types_id",
    "title": "Update a program type",
    "version": "0.1.0",
    "name": "Update__programsTypes__program_types_id",
    "group": "Program_Types",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "program_type_names",
            "description": "<p>Program_type_names information.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "2..2",
            "optional": true,
            "field": "program_type_names.lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": true,
            "field": "program_type_names.name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/program_type.py",
    "groupTitle": "Program_Types"
  },
  {
    "type": "delete",
    "url": "/programs/:programs_id",
    "title": "Delete a program",
    "version": "0.1.0",
    "name": "DELETE__programs__programs_id",
    "group": "Programs",
    "filename": "../odin/data/resources/program.py",
    "groupTitle": "Programs"
  },
  {
    "type": "get",
    "url": "/programs",
    "title": "Get all programs",
    "version": "0.1.0",
    "name": "GET__programs",
    "group": "Programs",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The program ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "program_types_id",
            "description": "<p>The program_type.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/programs.py",
    "groupTitle": "Programs"
  },
  {
    "type": "get",
    "url": "/programs/:programs_id",
    "title": "Get a program",
    "version": "0.1.0",
    "name": "GET__programs__programs_id",
    "group": "Programs",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The program ID</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "program_types_id",
            "description": "<p>The program_type.</p>"
          },
          {
            "group": "Success 200",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/program.py",
    "groupTitle": "Programs"
  },
  {
    "type": "post",
    "url": "/programs",
    "title": "Create a program",
    "version": "0.1.0",
    "name": "POST__programs",
    "group": "Programs",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "program_types_id",
            "description": "<p>The program_type.</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": false,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "program_names",
            "description": "<p>Program_names information.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "2..2",
            "optional": false,
            "field": "program_names.lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": false,
            "field": "program_names.name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/programs.py",
    "groupTitle": "Programs"
  },
  {
    "type": "update",
    "url": "/programs/:programs_id",
    "title": "Update a program",
    "version": "0.1.0",
    "name": "UPDATE__programs__programs_id",
    "group": "Programs",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "program_types_id",
            "description": "<p>The program_type.</p>"
          },
          {
            "group": "Parameter",
            "type": "Boolean",
            "optional": true,
            "field": "is_active",
            "description": "<p>If its active.</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "program_names",
            "description": "<p>Program_names information.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "2..2",
            "optional": true,
            "field": "program_names.lang",
            "description": "<p>The language.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "size": "..50",
            "optional": true,
            "field": "program_names.name",
            "description": "<p>The name.</p>"
          }
        ]
      }
    },
    "filename": "../odin/data/resources/program.py",
    "groupTitle": "Programs"
  },
  {
    "type": "delete",
    "url": "/researcher/profiles/:researcher_profile_id",
    "title": "Delete a researcher profile",
    "version": "0.1.0",
    "name": "DELETE__researcher_profiles__researcher_profile_id",
    "group": "Researcher_Profile",
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
    "filename": "../odin/data/resources/researcher_profile.py",
    "groupTitle": "Researcher_Profile"
  },
  {
    "type": "get",
    "url": "/researcher/profiles",
    "title": "Get all researcher profiles",
    "version": "0.1.0",
    "name": "GET__researcher_profiles",
    "group": "Researcher_Profile",
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
    "filename": "../odin/data/resources/researcher_profiles.py",
    "groupTitle": "Researcher_Profile"
  },
  {
    "type": "get",
    "url": "/researcher/profiles/:researcher_profile_id",
    "title": "Get a researcher profile",
    "version": "0.1.0",
    "name": "GET__researcher_profiles__researcher_profile_id",
    "group": "Researcher_Profile",
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
    "filename": "../odin/data/resources/researcher_profile.py",
    "groupTitle": "Researcher_Profile"
  },
  {
    "type": "post",
    "url": "/researcher/profiles",
    "title": "Create a researcher profile",
    "version": "0.1.0",
    "name": "POST__researcher_profiles",
    "group": "Researcher_Profile",
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
    "filename": "../odin/data/resources/researcher_profiles.py",
    "groupTitle": "Researcher_Profile"
  },
  {
    "type": "update",
    "url": "/researcher/profiles/:researcher_profile_id",
    "title": "Update a researcher profile",
    "version": "0.1.0",
    "name": "UPDATE__researcher_profiles__researcher_profile_id",
    "group": "Researcher_Profile",
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
    "filename": "../odin/data/resources/researcher_profile.py",
    "groupTitle": "Researcher_Profile"
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "../odin/apidoc/main.js",
    "group": "_home_medtech_Public_odin_apidoc_main_js",
    "groupTitle": "_home_medtech_Public_odin_apidoc_main_js",
    "name": ""
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "../odin/doc/main.js",
    "group": "_home_medtech_Public_odin_doc_main_js",
    "groupTitle": "_home_medtech_Public_odin_doc_main_js",
    "name": ""
  }
] });
