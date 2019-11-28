from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):
    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.organizations_table = Table('organizations', self.metadata, autoload = True)
        self.organization_names_table = Table('organization_names', self.metadata, autoload = True)

    def get(self):
        stmt = select([self.organizations_table.c.id.label('id'),
                       self.organizations_table.c.parent_id.label('parent_id'),
                       self.organizations_table.c.organization_types_id.label('organization_types_id'),
                       self.organizations_table.c.date_created.label('date_created'),
                       self.organizations_table.c.is_active.label('is_active'),
                       self.organization_names_table.c.lang.label('lang'),
                       self.organization_names_table.c.name.label('name'),
                       self.organization_names_table.c.full_path.label('full_path')]).\
            select_from(self.organizations_table
                        .join(self.organization_names_table)).\
            apply_labels()
            
        results = self.connection.execute(stmt).fetchall()
        return results

# Instantiated once when the odin app loads rather than on every call.
organizations = Model()
