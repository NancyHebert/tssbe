from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.program_types_table = Table('program_types', self.metadata, autoload = True)
        self.program_type_names_table = Table('program_type_names', self.metadata, autoload = True)

    def get(self):
        stmt = select([self.program_types_table.c.id.label('id'),
                       self.program_types_table.c.date_created.label('date_created'),
                       self.program_types_table.c.is_active.label('is_active'),
                       self.program_type_names_table.c.lang.label('lang'),
                       self.program_type_names_table.c.name.label('name'),
                       self.program_type_names_table.c.full_path.label('full_path')]).\
            select_from(self.program_types_table
                        .join(self.program_type_names_table)).\
            apply_labels()

        results = self.connection.execute(stmt).fetchall()
        return results

# Instantiated once when the odin app loads rather than on every call.
program_types = Model()
