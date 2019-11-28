from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel
from data.models.utils.stats import mean, median

class Model(PGModel):
    # Note: reports_students_grid has very similar code.
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

        (
            internal_students_count,
            external_students_count,
            level_of_instruction_list
        ) = self.process_students(profile_list)

        researchers_contacted_counts = self.count_researchers(researchers_contacted_list)
        mean_researchers_contacted = mean(researchers_contacted_counts)
        median_researchers_contacted = median(researchers_contacted_counts)

        messages_sent_counts = self.count_messages(messages_sent_count_list)
        mean_messages_sent = mean(messages_sent_counts)
        median_messages_sent = median(messages_sent_counts)

        # Load the results object and we're done
        results = {
            'student': student_list,
            'internal_students_count': internal_students_count,
            'external_students_count': external_students_count,
            'level': level_of_instruction_list,
            'mean_researchers_contacted': mean_researchers_contacted,
            'median_researchers_contacted': median_researchers_contacted,
            'mean_messages_sent': mean_messages_sent,
            'median_messages_sent': median_messages_sent
        }

        return results


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

            researchers_contacted = [researcher['researcher_name']
                                     for researcher in researchers_contacted_list
                                     if researcher['student_username'] == profile['username']]
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


    def process_students(self, profile_list):
        # internal_students_count = 5
        # external_students_count = 7
        # level_of_instruction_list = [{
        #     'level_of_instruction': 'msc',
        #     'count': 4
        # }, {
        #     'level_of_instruction': 'phd',
        #     'count': 8
        # }]

        internal_students_count = 0
        external_students_count = 0
        level_of_instruction_list = []

        for profile in profile_list:
            if '@' in profile['username']:
                external_students_count += 1
            else:
                internal_students_count += 1

            found = False
            for level in level_of_instruction_list:

                if level['level_of_instruction'] == profile['level_of_instruction']:
                    found = True
                    level['count'] += 1
                    break

            if not found:
                result_dict = {
                    'level_of_instruction': profile['level_of_instruction'],
                    'count': 1
                }
                level_of_instruction_list.append(result_dict)

        return (internal_students_count, external_students_count, level_of_instruction_list)

    def count_researchers(self, researchers_contacted_list):
        results = []
        prev_student = ''
        researchers_count = 0
        first_time_through = True

        researchers_contacted_list = sorted(
            researchers_contacted_list,
            key=lambda contact: contact["student_username"]
            )
        for contact in researchers_contacted_list:
            if contact["student_username"] == prev_student:
                researchers_count += 1
            else:
                if first_time_through:
                    first_time_through = False
                else:
                    results.append(researchers_count)
                prev_student = contact["student_username"]
                researchers_count = 1

        # After loop, save any remaining data
        if researchers_count > 0:
            results.append(researchers_count)

        return results

    def count_messages(self, messages_sent_count_list):
        results = []
        for messages_sent_count in messages_sent_count_list:
            messages_count = messages_sent_count['messages_sent']
            results.append(messages_count)

        return results

# Instantiated once when the odin app loads rather than on every call.
reports_students = Model()
