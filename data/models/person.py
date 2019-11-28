from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.people_table = Table('people', self.metadata, autoload = True)
        self.person_type_rel_table = Table('person_type_rel', self.metadata, autoload = True)

    def get(self, people_id):
        stmt = select([self.people_table.c.id.label('id'),
                       self.people_table.c.first_name.label('first_name'),
                       self.people_table.c.middle_initial.label('middle_initial'),
                       self.people_table.c.last_name.label('last_name'),
                       self.people_table.c.date_of_birth.label('date_of_birth')]).\
            where(self.people_table.c.id == people_id).\
            apply_labels()

        results = self.connection.execute(stmt)
        return results

    def post(self, people_json):
        transaction = self.connection.begin()
        try:
            stmt = self.people_table.insert().\
                values(first_name = people_json['first_name'],
                       middle_initial = people_json['middle_initial'],
                       last_name = people_json['last_name'],
                       date_of_birth = people_json['date_of_birth'])

            results = self.connection.execute(stmt)
            people_id = results.inserted_primary_key[0]

            stmt = self.person_type_rel_table.insert().\
                values(person_types_id = people_json['person_types_id'],
                       people_id = people_id)

            results = self.connection.execute(stmt)
            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def delete(self, people_id):
        transaction = self.connection.begin()
        try:
            stmt = self.people_table.update().\
                values(is_active = False).\
                where(self.people_table.c.id == people_id)

            results = self.connection.execute(stmt)
            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def update(self, people_id, people_json):
        #Todo doesn't handle person_types_id
        transaction = self.connection.begin()
        try:
            stmt = self.people_table.update().\
                where(self.people_table.c.id == people_id).\
                values(people_json)

            self.connection.execute(stmt)

            transaction.commit()
            return
        except:
            transaction.rollback()
            raise

# Instantiated once when the odin app loads rather than on every call.
person = Model()
