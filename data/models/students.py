from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.students_table = Table('students', self.metadata, autoload = True) # handle error

    def get(self):
        try:
            #handle error
            self.connection = self.db_engine.connect()
            stmt = select([self.students_table.c.username,
                       self.students_table.c.name,
                       self.students_table.c.email,
                    #    self.students_table.c.program_id,
                       self.students_table.c.program_code,
                       self.students_table.c.admitted,
                    #    self.students_table.c.student_number,
                       self.students_table.c.level_of_instruction,
                       self.students_table.c.date_created,
                    #    self.students_table.c.is_confirmed,
                       self.students_table.c.is_active])

            results = self.connection.execute(stmt).fetchall()
            return results
        finally:
            self.connection.close()

# Instantiated once when the odin app loads rather than on every call.
students = Model()
