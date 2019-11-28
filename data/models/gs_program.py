from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.gs_programs_table = Table('gs_programs', self.metadata, autoload = True) # handle error

    def get(self, code, lang='en'):
        try:
            #handle error
            self.connection = self.db_engine.connect()
            stmt = select([self.gs_programs_table.c.id,
                        self.gs_programs_table.c.code,
                        self.gs_programs_table.c.name,
                        self.gs_programs_table.c.lang]).\
                where(self.gs_programs_table.c.code == code).\
                where(self.gs_programs_table.c.lang == lang)
            results = self.connection.execute(stmt).fetchone()
            return results
        finally:
            self.connection.close()


# Instantiated once when the odin app loads rather than on every call.
gs_program = Model()
