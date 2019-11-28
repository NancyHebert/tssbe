from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel

import datetime


class Model(PGModel):
    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, *args, **kwargs)
        self.organization_types_table = Table('organization_types', self.metadata, autoload = True)
        self.organization_type_names_table = Table('organization_type_names', self.metadata, autoload = True)

    def get(self, organization_types_id):
        stmt = select([self.organization_types_table.c.id.label('id'),
                       self.organization_types_table.c.is_active.label('is_active'),
                       self.organization_types_table.c.date_created.label('date_created'),
                       self.organization_type_names_table.c.lang.label('lang'),
                       self.organization_type_names_table.c.name.label('name')]).\
            select_from(self.organization_types_table
                        .join(self.organization_type_names_table)).\
            where(self.organization_types_table.c.id == organization_types_id).\
            apply_labels()

        results = self.connection.execute(stmt)
        return results

    def post(self, organization_types_json):
        transaction = self.connection.begin()
        try:
            stmt = self.organization_types_table.insert().\
                values(is_active = True)

            results = self.connection.execute(stmt)
            organization_types_id = results.inserted_primary_key[0]

            for organization_type_names_json in organization_types_json['organization_type_names']:
                stmt = self.organization_type_names_table.insert().\
                    values(organization_types_id = organization_types_id,
                           lang = organization_type_names_json['lang'],
                           name = organization_type_names_json['name'])
                self.connection.execute(stmt)

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def delete(self, organization_types_id):
        transaction = self.connection.begin()
        try:
            stmt = self.organization_types_table.update().\
                values(is_active = False).\
                where(self.organization_types_table.c.id == organization_types_id)

            results = self.connection.execute(stmt)
            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def put(self, organization_types_id, organization_types_json):
        transaction = self.connection.begin()
        try:
            first_level_json = { k:v for (k, v) in organization_types_json.items() if k != 'organization_type_names'}

            stmt = self.organization_types_table.update().\
                where(self.organization_types_table.c.id == organization_types_id).\
                values(first_level_json)

            self.connection.execute(stmt)

            if 'organization_type_names' in organization_types_json:
                for organization_type_names_json in organization_types_json['organization_type_names']:
                    stmt = self.organization_type_names_table.update().\
                        values(organization_type_names_json).\
                        where(self.organization_type_names_table.c.lang == organization_type_names_json['lang']).\
                        where(self.organization_type_names_table.c.organization_types_id == organization_types_id)
                    self.connection.execute(stmt)

            transaction.commit()
            return
        except:
            transaction.rollback()
            raise


# Instantiated once when the odin app loads rather than on every call.
organization_type = Model()
