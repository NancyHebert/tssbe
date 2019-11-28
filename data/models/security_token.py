from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel
import uuid

class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.security_tokens_table = Table('security_tokens', self.metadata, autoload = True)

    def get(self, app_name):
        stmt = select([self.security_tokens_table.c.token.label('token'),
                       self.security_tokens_table.c.app_name.label('app_name'),
                       self.security_tokens_table.c.host.label('host'),
                       self.security_tokens_table.c.is_active.label('is_active')]).\
            where(self.security_tokens_table.c.app_name == app_name).\
            where(self.security_tokens_table.c.is_active == True).\
            apply_labels()

        results = self.connection.execute(stmt)
        return results

    def post(self, token_json):
        transaction = self.connection.begin()
        try:
            stmt = self.security_tokens_table.insert().\
                values(token = token_json['token'],
                       app_name = token_json['app_name'],
                       host = token_json['host'],
                       is_active = True)

            results = self.connection.execute(stmt)
            token = results.inserted_primary_key

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise

    def delete(self, app_name):
        transaction = self.connection.begin()
        try:
            stmt = self.security_tokens_table.update().\
                values(is_active = False).\
                where(self.security_tokens_table.c.app_name == app_name)

            results = self.connection.execute(stmt)
            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise


# Instantiated once when the odin app loads rather than on every call.
security_token = Model()
