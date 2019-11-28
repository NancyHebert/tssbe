from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.conversations_table = Table('conversations', self.metadata, autoload = True)

    def get(self):
        try:
            self.connection = self.db_engine.connect()
            stmt = select([self.conversations_table.c.id,
                       self.conversations_table.c.researcher_uniweb_number,
                       self.conversations_table.c.researcher_name,
                       self.conversations_table.c.student_username,
                       self.conversations_table.c.student_name,
                       self.conversations_table.c.body,
                       self.conversations_table.c.is_from_student,
                       self.conversations_table.c.is_draft,
                       self.conversations_table.c.sent_date,
                       self.conversations_table.c.read_date]).\
              order_by(self.conversations_table.c.sent_date)

            results = self.connection.execute(stmt).fetchall()
            return results
        finally:
            self.connection.close()
    
    def getByStudentAndResearcher(self, studentUsername, researcherId):
        try:
            self.connection = self.db_engine.connect()
            stmt = select([self.conversations_table.c.id,
                       self.conversations_table.c.researcher_uniweb_number,
                       self.conversations_table.c.researcher_name,
                       self.conversations_table.c.student_username,
                       self.conversations_table.c.student_name,
                       self.conversations_table.c.body,
                       self.conversations_table.c.is_from_student,
                       self.conversations_table.c.is_draft,
                       self.conversations_table.c.sent_date,
                       self.conversations_table.c.read_date]).\
              where(self.conversations_table.c.student_username == studentUsername).\
              where(self.conversations_table.c.researcher_uniweb_number == researcherId).\
              order_by(self.conversations_table.c.sent_date)

            results = self.connection.execute(stmt).fetchall()
            return results
        finally:
            self.connection.close()


# Instantiated once when the odin app loads rather than on every call.
conversations = Model()
