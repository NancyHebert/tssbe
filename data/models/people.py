from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.people_table = Table('people', self.metadata, autoload = True)

    def get(self):
        stmt = select([self.people_table.c.id.label('id'),
                       self.people_table.c.first_name.label('first_name'),
                       self.people_table.c.middle_initial.label('middle_initial'),
                       self.people_table.c.last_name.label('last_name'),
                       self.people_table.c.date_of_birth.label('date_of_birth')]).\
            apply_labels()

        results = self.connection.execute(stmt).fetchall()
        return results

# Instantiated once when the odin app loads rather than on every call.
people = Model()
