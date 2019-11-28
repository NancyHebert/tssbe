from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel

import datetime


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.person_types_table = Table('person_types', self.metadata, autoload = True)
        self.person_type_names_table = Table('person_type_names', self.metadata, autoload = True)

    def get(self, person_types_id):
        stmt = select([self.person_types_table.c.id.label('id'),
                       self.person_types_table.c.parent_id.label('parent_id'),
                       self.person_types_table.c.date_created.label('date_created'),
                       self.person_types_table.c.is_active.label('is_active'),
                       self.person_type_names_table.c.lang.label('lang'),
                       self.person_type_names_table.c.name.label('name'),
                       self.person_type_names_table.c.full_path.label('full_path')]).\
            select_from(self.person_types_table
                        .join(self.person_type_names_table)).\
            where(self.person_types_table.c.id == person_types_id).\
            apply_labels()

        results = self.connection.execute(stmt)
        return results

    def post(self, person_types_json):
        transaction = self.connection.begin()
        try:
            stmt = self.person_types_table.insert().\
                values(parent_id = person_types_json['parent_id'],
                       is_active = True)

            results = self.connection.execute(stmt)
            person_types_id = results.inserted_primary_key[0]

            for person_type_names_json in person_types_json['person_type_names']:
                stmt = self.person_type_names_table.insert().\
                    values(person_types_id = person_types_id,
                           lang = person_type_names_json['lang'],
                           name = person_type_names_json['name'],
                           full_path = person_type_names_json['full_path'])
                self.connection.execute(stmt)

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def delete(self, person_types_id):
        transaction = self.connection.begin()
        try:
            stmt = self.person_types_table.update().\
                values(is_active = False).\
                where(self.person_types_table.c.id == person_types_id)

            results = self.connection.execute(stmt)
            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def update(self, person_types_id, person_types_json):       
        transaction = self.connection.begin()
        try:
            first_level_json = { k:v for (k, v) in person_types_json.items() if k != 'person_type_names'}

            stmt = self.person_types_table.update().\
                where(self.person_types_table.c.id == person_types_id).\
                values(first_level_json)

            self.connection.execute(stmt)

            if 'person_type_names' in person_types_json:
                for person_type_names_json in person_types_json['person_type_names']:
                    stmt = self.person_type_names_table.update().\
                        values(person_type_names_json).\
                        where(self.person_type_names_table.c.lang == person_type_names_json['lang']).\
                        where(self.person_type_names_table.c.person_types_id == person_types_id)
                    self.connection.execute(stmt)

            transaction.commit()
            return
        except:
            transaction.rollback()
            raise

# Instantiated once when the odin app loads rather than on every call.
person_type = Model()
