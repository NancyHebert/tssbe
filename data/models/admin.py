from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.admins_table = Table('admins', self.metadata, autoload = True)

    # def get(self, admin_id):
    #     try:
    #         #handle error
    #         self.connection = self.db_engine.connect()
    #         stmt = select([self.admins_table.c.id,
    #                    self.admins_table.c.name,
    #                    self.admins_table.c.email]).\
    #         where(self.admins_table.c.id == admin_id)

    #         results = self.connection.execute(stmt)
    #         return results
    #     finally:
    #         self.connection.close()
    
    def get_by_username(self, admin_username):
        try:
            self.connection = self.db_engine.connect()        
            stmt = select([self.admins_table.c.id,
                           self.admins_table.c.username,
                           self.admins_table.c.name,
                           self.admins_table.c.email]).\
                where(self.admins_table.c.username == admin_username)

            results = self.connection.execute(stmt).fetchone()
            return results
        except exc.StatementError:
            return None
        finally:
            self.connection.close()


    # def post(self, admins_json):
    #     try:
    #         self.connection = self.db_engine.connect()
    #         transaction = self.connection.begin()

    #         stmt = self.admins_table.insert().\
    #             values(
    #                     name = admins_json['name'],
    #                     email = admins_json['email']
    #                     )

    #         results = self.connection.execute(stmt)
    #         # admin_id = results.inserted_primary_key

    #         transaction.commit()
    #         return results
    #     except:
    #         transaction.rollback()
    #         raise
    #     finally:
    #         self.connection.close()



    # def update(self, admin_id, admins_json):
    #     try:
    #         self.connection = self.db_engine.connect()
    #         transaction = self.connection.begin()

    #         stmt = self.admins_table.update().\
    #             where(self.admins_table.c.id == admin_id).\
    #             values(admins_json)

    #         results = self.connection.execute(stmt)

    #         transaction.commit()
    #         return results
    #     except:
    #         transaction.rollback()
    #         raise
    #     finally:
    #         self.connection.close()

# Instantiated once when the odin app loads rather than on every call.
admin = Model()
