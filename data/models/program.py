from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel

import datetime


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.programs_table = Table('programs', self.metadata, autoload = True)
        self.program_names_table = Table('program_names', self.metadata, autoload = True)

    def get(self, programs_id):
        stmt = select([self.programs_table.c.id.label('id'),
                       self.programs_table.c.program_types_id.label('program_types_id'),
                       self.programs_table.c.date_created.label('date_created'),
                       self.programs_table.c.is_active.label('is_active'),
                       self.program_names_table.c.lang.label('lang'),
                       self.program_names_table.c.name.label('name')]).\
            select_from(self.programs_table
                        .join(self.program_names_table)).\
            where(self.programs_table.c.id == programs_id).\
            apply_labels()

        results = self.connection.execute(stmt)
        return results

    def post(self, programs_json):
        transaction = self.connection.begin()

        try:
            stmt = self.programs_table.insert().\
                values(program_types_id = programs_json['program_types_id'],
                       is_active = True)

            results = self.connection.execute(stmt)
            programs_id = results.inserted_primary_key[0]

            for program_names_json in programs_json['program_names']:
                stmt = self.program_names_table.insert().\
                    values(programs_id = programs_id,
                           lang = program_names_json['lang'],
                           name = program_names_json['name'],
                           full_path = program_names_json['full_path'])
                self.connection.execute(stmt)

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def delete(self, programs_id):
        transaction = self.connection.begin()
        try:
            stmt = self.programs_table.update().\
                values(is_active = False).\
                where(self.programs_table.c.id == programs_id)

            results = self.connection.execute(stmt)
            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def put(self, programs_id, programs_json):
        transaction = self.connection.begin()
        try:
            first_level_json = { k:v for (k, v) in programs_json.items() if k != 'program_names'}

            stmt = self.programs_table.update().\
                where(self.programs_table.c.id == programs_id).\
                values(first_level_json)

            self.connection.execute(stmt)

            if 'program_names' in programs_json:
                for program_names_json in programs_json['program_names']:
                    stmt = self.program_names_table.update().\
                        values(program_names_json).\
                        where(self.program_names_table.c.lang == program_names_json['lang']).\
                        where(self.program_names_table.c.programs_id == programs_id)
                    self.connection.execute(stmt)

            transaction.commit()
            return
        except:
            transaction.rollback()
            raise

# Instantiated once when the odin app loads rather than on every call.
program = Model()
