from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.programs_table = Table('programs', self.metadata, autoload = True)
        self.program_names_table = Table('program_names', self.metadata, autoload = True)

    def get(self):
        stmt = select([self.programs_table.c.id.label('id'),
                       self.programs_table.c.program_types_id.label('program_types_id'),
                       self.programs_table.c.date_created.label('date_created'),
                       self.programs_table.c.is_active.label('is_active'),
                       self.program_names_table.c.lang.label('lang'),
                       self.program_names_table.c.name.label('name')]).\
            select_from(self.programs_table
                        .join(self.program_names_table)).\
            apply_labels()

        results = self.connection.execute(stmt).fetchall()
        return results

# Instantiated once when the odin app loads rather than on every call.
programs = Model()
