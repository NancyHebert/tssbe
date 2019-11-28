from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.person_types_table = Table('person_types', self.metadata, autoload = True)
        self.person_type_names_table = Table('person_type_names', self.metadata, autoload = True)

    def get(self):
        stmt = select([self.person_types_table.c.id.label('id'),
                       self.person_types_table.c.parent_id.label('parent_id'),
                       self.person_types_table.c.date_created.label('date_created'),
                       self.person_types_table.c.is_active.label('is_active'),
                       self.person_type_names_table.c.lang.label('lang'),
                       self.person_type_names_table.c.name.label('name'),
                       self.person_type_names_table.c.full_path.label('full_path')]).\
            select_from(self.person_types_table
                        .join(self.person_type_names_table)).\
            apply_labels()

        results = self.connection.execute(stmt).fetchall()
        return results

# Instantiated once when the odin app loads rather than on every call.
person_types = Model()
