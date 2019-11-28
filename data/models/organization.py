from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel

import datetime


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.organizations_table = Table('organizations', self.metadata, autoload = True)
        self.organization_names_table = Table('organization_names', self.metadata, autoload = True)

    def get(self, organizations_id):
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
            where(self.organizations_table.c.id == organizations_id).\
            apply_labels()

        results = self.connection.execute(stmt)
        return results

    def post(self, organizations_json):
        transaction = self.connection.begin()
        try:
            stmt = self.organizations_table.insert().\
                values(parent_id = organizations_json['parent_id'],
                       organization_types_id = organizations_json['organization_types_id'],
                       is_active = True)

            results = self.connection.execute(stmt)
            organizations_id = results.inserted_primary_key[0]

            for organization_names_json in organizations_json['organization_names']:
                stmt = self.organization_names_table.insert().\
                    values(organizations_id = organizations_id,
                           lang = organization_names_json['lang'],
                           name = organization_names_json['name'],
                           full_path = organization_names_json['full_path'])
                self.connection.execute(stmt)

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def delete(self, organizations_id):
        transaction = self.connection.begin()
        try:
            stmt = self.organizations_table.update().\
                values(is_active = False).\
                where(self.organizations_table.c.id == organizations_id)

            results = self.connection.execute(stmt)
            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def update(self, organizations_id, organizations_json):
        transaction = self.connection.begin()
        try:
            first_level_json = { k:v for (k, v) in organizations_json.items() if k != 'organization_names'}

            stmt = self.organizations_table.update().\
                where(self.organizations_table.c.id == organizations_id).\
                values(first_level_json)

            self.connection.execute(stmt)

            if 'organization_names' in organizations_json:
                for organization_names_json in organizations_json['organization_names']:
                    stmt = self.organization_names_table.update().\
                        values(organization_names_json).\
                        where(self.organization_names_table.c.lang == organization_names_json['lang']).\
                        where(self.organization_names_table.c.organizations_id == organizations_id)
                    self.connection.execute(stmt)

            transaction.commit()
            return
        except:
            transaction.rollback()
            raise

organization = Model()
