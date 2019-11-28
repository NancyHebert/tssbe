from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel

import datetime


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.program_types_table = Table('program_types', self.metadata, autoload = True)
        self.program_type_names_table = Table('program_type_names', self.metadata, autoload = True)

    def get(self, program_types_id):
        stmt = select([self.program_types_table.c.id.label('id'),
                       self.program_types_table.c.date_created.label('date_created'),
                       self.program_types_table.c.is_active.label('is_active'),
                       self.program_type_names_table.c.lang.label('lang'),
                       self.program_type_names_table.c.name.label('name'),
                       self.program_type_names_table.c.full_path.label('full_path')]).\
            select_from(self.program_types_table
                        .join(self.program_type_names_table)).\
            where(self.program_types_table.c.id == program_types_id).\
            apply_labels()

        results = self.connection.execute(stmt)
        return results

    def post(self, program_types_json):
        transaction = self.connection.begin()
        try:
            stmt = self.program_types_table.insert().\
                values(is_active = True)

            results = self.connection.execute(stmt)
            program_types_id = results.inserted_primary_key[0]

            for program_type_names_json in program_types_json['program_type_names']:
                stmt = self.program_type_names_table.insert().\
                    values(program_types_id = program_types_id,
                           lang = program_type_names_json['lang'],
                           name = program_type_names_json['name'],
                           full_path = program_type_names_json['full_path'])
                self.connection.execute(stmt)

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def delete(self, program_types_id):
        transaction = self.connection.begin()
        try:
            stmt = self.program_types_table.update().\
                values(is_active = False).\
                where(self.program_types_table.c.id == program_types_id)

            results = self.connection.execute(stmt)
            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def put(self, program_types_id, program_types_json):
        transaction = self.connection.begin()
        try:
            first_level_json = { k:v for (k, v) in program_types_json.items() if k != 'program_type_names'}

            stmt = self.program_types_table.update().\
                where(self.program_types_table.c.id == program_types_id).\
                values(first_level_json)

            self.connection.execute(stmt)

            if 'program_type_names' in program_types_json:
                for program_type_names_json in program_types_json['program_type_names']:
                    stmt = self.program_type_names_table.update().\
                        values(program_type_names_json).\
                        where(self.program_type_names_table.c.lang == program_type_names_json['lang']).\
                        where(self.program_type_names_table.c.program_types_id == program_types_id)
                    self.connection.execute(stmt)

            transaction.commit()
            return
        except:
            transaction.rollback()
            raise

# Instantiated once when the odin app loads rather than on every call.
program_type = Model()
