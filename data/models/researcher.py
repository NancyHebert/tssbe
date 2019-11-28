from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.researchers_table = Table('researchers', self.metadata, autoload = True)
    
    def get(self, uniweb_number):
        try:
            #handle error
            self.connection = self.db_engine.connect()
            stmt = select([self.researchers_table.c.available_date]).\
                where(self.researchers_table.c.uniweb_number == uniweb_number)

            results = self.connection.execute(stmt)
            return results.fetchall()
        finally:
            self.connection.close()

    def update(self, uniweb_number, researchers_json):
        try:
            res = self.get(uniweb_number)

            #handle error
            self.connection = self.db_engine.connect()
            transaction = self.connection.begin()

            if len(res) > 0: # Researcher exists in this table
                avail_date = researchers_json['available_date']
                if not (avail_date and avail_date.strip()): # Check for null or blank
                    avail_date = None

                stmt = self.researchers_table.update().\
                    where(self.researchers_table.c.uniweb_number == uniweb_number).\
                    values(
                        available_date = avail_date
                        )
            else: # Create the researcher in this table
                stmt = self.researchers_table.insert().\
                    values(
                        uniweb_number = uniweb_number,
                        available_date = researchers_json['available_date']
                        )

            results = self.connection.execute(stmt)

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise
        finally:
            self.connection.close()

# Instantiated once when the odin app loads rather than on every call.
researcher = Model()
