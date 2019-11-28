from sqlalchemy import *
from sqlalchemy.exc import StatementError
from data.models.utils.postgres_mixin import PGModel


class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.students_table = Table('students', self.metadata, autoload = True)

    def get(self, username):
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
                       self.students_table.c.is_active]).\
            where(self.students_table.c.username == username)

            results = self.connection.execute(stmt).fetchone()
            return results
        except StatementError:
            return None
        finally:
            self.connection.close()

    def get_by_email(self, student_email):
        try:
            self.connection = self.db_engine.connect()
            stmt = select([self.students_table.c.id,
                            self.students_table.c.username,
                            self.students_table.c.name,
                            self.students_table.c.email,
                            self.students_table.c.program_code,
                            self.students_table.c.admitted,
                            self.students_table.c.level_of_instruction,
                            self.students_table.c.date_created,
                            self.students_table.c.is_active]).\
                where(self.students_table.c.email == student_email)

            results = self.connection.execute(stmt).fetchone()
            return results
        finally:
            self.connection.close()


    def post(self, students_json):

        # Allow for missing parameters
        try:
            program_code = int(students_json['program_code'])
        except KeyError:
            program_code = None

        try:
            admitted = students_json['admitted'],
        except KeyError:
            admitted = None

        try:
            level_of_instruction = students_json['level_of_instruction']
        except KeyError:
            level_of_instruction = None

        try:
            self.connection = self.db_engine.connect()
            transaction = self.connection.begin()

            stmt = self.students_table.insert().\
                values(
                    username=students_json['username'],
                    name=students_json['name'],
                    email=students_json['email'],
                    program_code=program_code,
                    admitted=admitted,
                    level_of_instruction=level_of_instruction
                    )

            results = self.connection.execute(stmt)
            # student_id = results.inserted_primary_key

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise
        finally:
            self.connection.close()

    # def postbyid(self, student_id, students_json):
    #     transaction = self.connection.begin()
    #     try:
    #         res = self.update(student_id, students_json) # find the student record

    #         transaction.commit()
    #         self.connection.execute(stmt)

    #         transaction.commit()
    #         return
    #     except:
    #         transaction.rollback()
    #         raise


    # def delete(self, student_id):
    #     transaction = self.connection.begin()
    #     try:
    #         stmt = self.students_table.update().\
    #             values(is_active = False).\
    #             where(self.students_table.c.id == student_id)

    #         results = self.connection.execute(stmt)
    #         transaction.commit()
    #         return results
    #     except:
    #         transaction.rollback()
    #         raise


    def update(self, username, students_json):
        try:
            self.connection = self.db_engine.connect()
            transaction = self.connection.begin()

            stmt = self.students_table.update().\
                where(self.students_table.c.username == username).\
                values(students_json)

            results = self.connection.execute(stmt)

            transaction.commit()
            return results
        except:
            transaction.rollback()
            raise
        finally:
            self.connection.close()

# Instantiated once when the odin app loads rather than on every call.
student = Model()
