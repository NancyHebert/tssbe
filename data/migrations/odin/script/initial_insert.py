from sqlalchemy import *
import json
import os
import sys
sys.path.append(os.path.realpath(__file__ + '/../../../../models/utils'))
from postgres_mixin import PGModel


class Script(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.organizations_table = Table('organizations', self.metadata, autoload=True)
        self.organization_names_table = Table('organization_names', self.metadata, autoload=True)
        self.organization_types_table = Table('organization_types', self.metadata, autoload=True)
        self.organization_type_names_table = Table('organization_type_names', self.metadata, autoload=True)
        self.people_table = Table('people', self.metadata, autoload=True)
        self.person_types_table = Table('person_types', self.metadata, autoload=True)
        self.person_type_names_table = Table('person_type_names', self.metadata, autoload=True)
        self.person_type_rel_table = Table('person_type_rel', self.metadata, autoload=True)

    def insert_person_types(self):
        with open('./json/person_types.json') as data_file:
            person_types_json = json.load(data_file)

        transaction = self.connection.begin()
        try:
            for person_types_dict in person_types_json:
                stmt = self.person_types_table.insert(). \
                    values(parent_id=person_types_dict['parent_id'],
                           is_active=bool(person_types_dict['is_active']))

                results = self.connection.execute(stmt)
                person_types_id = results.inserted_primary_key

                for person_type_names_json in person_types_dict['person_type_names']:
                    stmt = self.person_type_names_table.insert(). \
                        values(person_types_id=person_types_id[0],
                               lang=person_type_names_json['lang'],
                               name=person_type_names_json['name'],
                               full_path=person_type_names_json['full_path'])
                    self.connection.execute(stmt)

            transaction.commit()
        except:
            transaction.rollback()
            raise

    def insert_people(self):
        with open('./json/people.json') as data_file:
            people_json = json.load(data_file)

        for people_dict in people_json:
            transaction = self.connection.begin()
            try:
                stmt = self.people_table.insert(). \
                    values(first_name=people_dict['first_name'],
                           middle_initial=people_dict['middle_name'],
                           last_name=people_dict['last_name'],
                           date_of_birth=people_dict['date_of_birth'])

                results = self.connection.execute(stmt)
                people_id = results.inserted_primary_key

                stmt = self.person_type_rel_table.insert(). \
                    values(person_types_id=people_dict['person_types_id'],
                           people_id=people_id[0])

                self.connection.execute(stmt)
                transaction.commit()
            except:
                transaction.rollback()
                raise

    def insert_organization_types(self):
        with open('./json/organization_types.json') as data_file:
            organization_types_json = json.load(data_file)

        for organization_types_dict in organization_types_json:
            transaction = self.connection.begin()
            try:
                stmt = self.organization_types_table.insert(). \
                    values(is_active=bool(organization_types_dict['is_active']))

                results = self.connection.execute(stmt)
                organization_types_id = results.inserted_primary_key

                for organization_type_names_json in organization_types_dict['organization_type_names']:
                    stmt = self.organization_type_names_table.insert(). \
                        values(organization_types_id=organization_types_id[0],
                               lang=organization_type_names_json['lang'],
                               name=organization_type_names_json['name'])
                    self.connection.execute(stmt)

                transaction.commit()
            except:
                transaction.rollback()
                raise

    def insert_organization(self):
        with open('./json/organizations.json') as data_file:
            organizations_json = json.load(data_file)

        transaction = self.connection.begin()
        try:
            for organizations_dict in organizations_json:
                stmt = self.organizations_table.insert(). \
                    values(parent_id=organizations_dict['parent_id'],
                           organization_types_id=organizations_dict['organization_types_id'],
                           is_active=bool(organizations_dict['is_active']))

                results = self.connection.execute(stmt)
                organizations_id = results.inserted_primary_key

                for organization_names_json in organizations_dict['organization_names']:
                    stmt = self.organization_names_table.insert(). \
                        values(organizations_id=organizations_id[0],
                               lang=organization_names_json['lang'],
                               name=organization_names_json['name'],
                               full_path=organization_names_json['full_path'])
                    self.connection.execute(stmt)

            transaction.commit()
        except Exception as e:
            transaction.rollback()
            raise

odin_insert_script = Script()

print('Starting to run script')

try:
    print('I am running insert on Person Types')
    odin_insert_script.insert_person_types()
    print('I am running insert on People')
    odin_insert_script.insert_people()
except:
    print('We have encounter a problem in the script')
    raise falcon.HTTPError(falcon.HTTP_400,
                           'Database Error',
                           'DB exception: %s' % e)

try:
    print('I am running insert on Organization Types')
    odin_insert_script.insert_organization_types()
    print('I am running insert on Organizations')
    odin_insert_script.insert_organization()
except:
    print('We have encounter a problem in the script')
    raise falcon.HTTPError(falcon.HTTP_400,
                           'Database Error',
                           'DB exception: %s' % e)

print('Script is done running')
