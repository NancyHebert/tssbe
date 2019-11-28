from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel

class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.conversations_table = Table('conversations', self.metadata, autoload = True)

    def getByToken(self, token):
        self.connection = self.db_engine.connect()
        stmt = select([self.conversations_table.c.id.label('id'),
                       self.conversations_table.c.researcher_uniweb_number.label('researcher_uniweb_number'),
                       self.conversations_table.c.researcher_name.label('researcher_name'),
                       self.conversations_table.c.student_username.label('student_username'),
                       self.conversations_table.c.student_name.label('student_name'),
                       self.conversations_table.c.body.label('body'),
                       self.conversations_table.c.sent_date.label('send_date'),
                       self.conversations_table.c.read_date.label('read_date'),
                       self.conversations_table.c.is_from_student.label('is_from_student'),
                       self.conversations_table.c.is_draft.label('is_draft'),
                       self.conversations_table.c.token.label('token')]).\
            select_from(self.conversations_table).\
            where(self.conversations_table.c.token == token).\
            apply_labels()

        results = self.connection.execute(stmt).fetchone()
        self.connection.close()
        return results

    def post(self, conversations_json):
        try:
            #handle error
            self.connection = self.db_engine.connect()
            transaction = self.connection.begin()

            stmt = self.conversations_table.insert().\
                values(
                        researcher_uniweb_number = conversations_json['researcher_uniweb_number'],
                        researcher_name = conversations_json['researcher_name'],
                        student_username = conversations_json['student_username'],
                        student_name = conversations_json['student_name'],
                        body = conversations_json['body'],
                        is_from_student = conversations_json['is_from_student'],
                        is_draft = conversations_json['is_draft'],
                        token = conversations_json['token']
                        )

            results = self.connection.execute(stmt)

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise
        finally:
            self.connection.close()


    def delete(self, conversation_id):
        self.connection = self.db_engine.connect()
        transaction = self.connection.begin()
        try:
            stmt = self.conversations_table.delete().\
                where(self.conversations_table.c.id == conversation_id)

            self.connection.execute(stmt)
            transaction.commit()
            return
        except:
            transaction.rollback()
            raise
        finally:
            self.connection.close()

    def update(self, id, conversations_json):
        try:
            self.connection = self.db_engine.connect()
            transaction = self.connection.begin()

            stmt = self.conversations_table.update().\
                where(self.conversations_table.c.id == id).\
                values(conversations_json)

            results = self.connection.execute(stmt)

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise
        finally:
            self.connection.close()

conversation = Model()
