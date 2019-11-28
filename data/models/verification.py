from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel
from data.resources.emails.email import Email
import random, string
from urllib.parse import quote_plus

class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.verifications_table = Table('verifications', self.metadata, autoload = True)

    def randomword(self, length):
        return ''.join(str(random.randint(0,9)) for i in range(length))

    def get(self, email, code):
        try:
            self.connection = self.db_engine.connect()
            stmt = select([self.verifications_table.c.code,
                          self.verifications_table.c.email]).\
                where(self.verifications_table.c.email == email).\
                where(self.verifications_table.c.code == code)
            return self.connection.execute(stmt).fetchone()
        finally:
            self.connection.close()

    def post(self, template, email):        
        try:
            # check if verification code already generated for this email
            self.connection = self.db_engine.connect()
            stmt = select([self.verifications_table.c.code,
                          self.verifications_table.c.email]).\
                where(self.verifications_table.c.email == email)

            result = self.connection.execute(stmt).fetchone()
            
            # Create a verification code if not already generated
            if result is None: 
                code = self.randomword(5)
                print('New verif code: ', code)
                isertStmt = self.verifications_table.insert().\
                    values(
                        email = email,
                        code = code
                        )
                self.connection.execute(isertStmt)
            else:
                code = result['code']

            # Email the code to user
            emailTemplate = 'password_reset' if template == 'password' else 'account_verification' if template == 'account' else None
            notificationEmail = Email(emailTemplate, **{'email': quote_plus(email), 'verification_code': code})
            notificationEmail.send(email)
            return
        except Exception as e:
            print('exception in verification post: ', e)
            raise
        finally:
            self.connection.close()

    def delete(self, email):
        try:
            #handle error
            self.connection = self.db_engine.connect()
            stmt = self.verifications_table.delete().\
                where(self.verifications_table.c.email == email)

            results = self.connection.execute(stmt)
        finally:
            self.connection.close()

# Instantiated once when the odin app loads rather than on every call.
verification = Model()
