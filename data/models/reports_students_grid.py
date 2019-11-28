from collections import OrderedDict
from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel

class Model(PGModel):
    # Note: reports_students has very similar code.
    # If you make updates here, consider making the same updates there.

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.students_table = Table('students', self.metadata, autoload=True)
        self.messages_table = Table('conversations', self.metadata, autoload=True)

    def get(self):
        try:
            # Use one connection for all the database work--but close it when finished.
            self.connection = self.db_engine.connect()

            profile_list = self.get_profiles()
            messages_sent_count_list = self.get_messages()
            researchers_contacted_list = self.get_researchers_contacted()

        finally:
            self.connection.close()

        # Perform further data manipulation as appropriate
        student_list = self.combine_lists(
            profile_list, researchers_contacted_list,
            messages_sent_count_list
            )
        student_list = self.final_cleanup(student_list)

        # And we're done
        return student_list


    def get_profiles(self):
        # results = [{
        #     'username': 'e@mail.ca',
        #     'profile_creation': datetime.now(),
        #     'name': 'student name',
        #     'email': 'e@mail.ca',
        #     'level_of_instruction': 'msc'
        # }, {
        #     'username': 'f@mail.ca',
        #     'profile_creation': datetime.now(),
        #     'name': 'student name 2',
        #     'email': 'f@mail.ca',
        #     'level_of_instruction': 'phd'
        # }]

        stmt = select([
            self.students_table.c.username,
            self.students_table.c.date_created.label('profile_creation'),
            self.students_table.c.name,
            self.students_table.c.email,
            self.students_table.c.level_of_instruction
            ]).\
            order_by(
                self.students_table.c.date_created
            )

        results = self.connection.execute(stmt).fetchall()
        results = [dict(r) for r in results]

        return results

    def get_messages(self):
        # results = [{
        #     'student_username': 'e@mail.ca',
        #     'messages_sent': 4
        # }, {
        #     'student_username': 'f@mail.ca',
        #     'messages_sent': 11
        # }]

        stmt = select([
            self.messages_table.c.student_username,
            func.count().label('messages_sent')]).\
            group_by(self.messages_table.c.student_username)

        results = self.connection.execute(stmt).fetchall()
        results = [dict(r) for r in results]

        return results

    def get_researchers_contacted(self):
        # results = [{
        #     'student_username': 'e@mail.ca',
        #     'researcher_name': 'Dr. One'
        # }, {
        #     'student_username': 'e@mail.ca',
        #     'researcher_name': 'Dr. Two'
        # }, {
        #     'student_username': 'e@mail.ca',
        #     'researcher_name': 'Dr. Three'
        # }, {
        #     'student_username': 'f@mail.ca',
        #     'researcher_name': 'Dr. Four'
        # }]

        stmt = \
            select([
                self.messages_table.c.student_username,
                func.max(self.messages_table.c.researcher_name).label('researcher_name')
            ]).\
            group_by(
                self.messages_table.c.student_username,
                self.messages_table.c.researcher_uniweb_number
            ).\
            order_by(
                self.messages_table.c.student_username,
                self.messages_table.c.researcher_uniweb_number
            )

        results = self.connection.execute(stmt).fetchall()
        results = [dict(r) for r in results]

        return results

    def combine_lists(self, profile_list, researchers_contacted_list, messages_sent_count_list):
        combined_list = []
        result_dict = {}

        for profile in profile_list:
            result_dict['username'] = profile['username']
            result_dict['profile_creation'] = profile['profile_creation']
            result_dict['name'] = profile['name']
            result_dict['email'] = profile['email']
            result_dict['level_of_instruction'] = profile['level_of_instruction']

            researchers_contacted_array = [researcher['researcher_name']
                                           for researcher in researchers_contacted_list
                                           if researcher['student_username'] == profile['username']]
            researchers_contacted = ", ".join(researchers_contacted_array)
            result_dict['researcher_names'] = researchers_contacted

            messages_sent = 0
            for message_count in messages_sent_count_list:
                if message_count['student_username'] == profile['username']:
                    messages_sent = message_count['messages_sent']
                    break
            result_dict['messages_sent'] = messages_sent

            combined_list.append(result_dict)
            result_dict = {}

        return combined_list

    def final_cleanup(self, student_list):
        # print('Entering final_cleanup')
        clean_results = []
        for student in student_list:
            result_dict = OrderedDict()

            result_dict['profile_creation'] = student['profile_creation']
            result_dict['name'] = student['name']
            result_dict['email'] = student['email']
            result_dict['level_of_instruction'] = student['level_of_instruction']
            result_dict['talked_with'] = student['researcher_names'] # Note that these are different
            result_dict['messages_sent'] = student['messages_sent']
            # result_dict['username'] = student['username']

            clean_results.append(result_dict)

        # print('Exiting final_cleanup')
        return clean_results

# Instantiated once when the odin app loads rather than on every call.
reports_students_grid = Model()
