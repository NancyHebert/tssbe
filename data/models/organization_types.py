from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):
    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, *args, **kwargs)
        self.organization_types_table = Table('organization_types', self.metadata, autoload = True)
        self.organization_type_names_table = Table('organization_type_names', self.metadata, autoload = True)

    def get(self):
        stmt = select([self.organization_types_table.c.id.label('id'),
                       self.organization_types_table.c.is_active.label('is_active'),
                       self.organization_types_table.c.date_created.label('date_created'),
                       self.organization_type_names_table.c.lang.label('lang'),
                       self.organization_type_names_table.c.name.label('name')]).\
            select_from(self.organization_types_table
                        .join(self.organization_type_names_table)).\
            apply_labels()

        results = self.connection.execute(stmt).fetchall()
        return results

# Instantiated once when the odin app loads rather than on every call.
organization_types = Model()
