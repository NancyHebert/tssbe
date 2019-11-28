import datetime
from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.researchers_table = Table('researchers', self.metadata, autoload=True)

    def get(self):
        current_date = datetime.date.today()
        try:
            self.connection = self.db_engine.connect()
            stmt = select([self.researchers_table.c.uniweb_number,
                           self.researchers_table.c.available_date]).\
                where(self.researchers_table.c.available_date > current_date)

            results = self.connection.execute(stmt)
            return results.fetchall()
        finally:
            self.connection.close()

# Instantiated once when the odin app loads rather than on every call.
researchers = Model()
