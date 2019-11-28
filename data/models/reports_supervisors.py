import json
from operator import itemgetter
from datetime import datetime, timedelta
import requests
from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel
from data.models.utils.stats import mean, median
from config.settings import config

class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.messages_table = Table('conversations', self.metadata, autoload=True)


    def get(self):
        # print('Entering get')
        self.connection = self.db_engine.connect()

        stmt = select([self.messages_table.c.researcher_uniweb_number,\
                       self.messages_table.c.student_username,\
                       self.messages_table.c.sent_date,\
                       self.messages_table.c.is_from_student]).\
            order_by(self.messages_table.c.researcher_uniweb_number,\
                     self.messages_table.c.student_username,\
                     self.messages_table.c.sent_date)

        try:
            results = self.connection.execute(stmt).fetchall()
        finally:
            self.connection.close()

        results = self.calculate_response_times(results)
        results = self.calculate_aggregate_values(results)
        results = self.sort_alphabetically(results)
        results = self.final_cleanup(results)

        # print('Exiting get')
        return results


    def calculate_response_times(self, results):
        # print('Entering calculate_response_times')
        prev_researcher = ""
        prev_student = ""
        processed_results = []
        result_dict = {}
        fast_forward = False
        good_conversation = True
        first_time_through = True

        for r in results:
            researcher = r[0]
            student = r[1]
            sent_date = r[2]
            is_from_student = r[3]

            if researcher == prev_researcher and student == prev_student and good_conversation:
                if fast_forward:
                    # Pass: we're only interested in the initial contact from
                    # the student and the first response from the researcher
                    pass
                else:
                    if is_from_student: # Sanity check: should be false
                        good_conversation = False
                        print('Second message in conversation between researcher %s' % researcher,
                              ' and student %s, dated %s, is from student' % (student, sent_date))
                    else:
                        good_conversation = True
                        # result_dict['response time'] = (sent_date - prev_sent_date).total_seconds() # use seconds for testing
                        result_dict['response time'] = (sent_date - prev_sent_date).days

                    fast_forward = True

            else: # New researcher or new student
                if first_time_through:
                    first_time_through = False
                else:
                    if good_conversation:
                        processed_results.append(result_dict)

                result_dict = {}
                result_dict['researcher_uniweb_number'] = researcher
                result_dict['student'] = student
                result_dict['response time'] = None

                prev_researcher = researcher
                prev_student = student
                prev_sent_date = sent_date
                fast_forward = False

                if is_from_student: # Sanity check: should be true
                    good_conversation = True
                else:
                    good_conversation = False
                    print('First message in conversation between researcher %s' % researcher,
                          ' and student %s, dated %s, is from researcher' % (student, sent_date))

        # End of for loop: write out last set of processed results
        if good_conversation and not first_time_through:
            processed_results.append(result_dict)

        # print('Exiting calculate_response_times')
        return processed_results


    def calculate_aggregate_values(self, processed_results):
        # print('Entering calculate_aggregate_values')
        aggregated_results = []
        result_dict = {}
        prev_researcher = ""
        response_times = []
        none_count = 0
        first_time_through = True

        for pr in processed_results:
            researcher = pr['researcher_uniweb_number']

            if researcher != prev_researcher:
                if first_time_through:
                    first_time_through = False
                else:
                    result_dict['uniweb_number'] = prev_researcher
                    if len(response_times) > 0:
                        result_dict['mean_response_time'] = mean(response_times)
                        response_times.sort()
                        result_dict['median_response_time'] = median(response_times)
                    result_dict['unreturned_contacts'] = none_count
                    aggregated_results.append(result_dict)
                    result_dict = {}

                    response_times = []
                    none_count = 0

                prev_researcher = researcher

            # Whether or not researcher is new, need to update response times info
            rt = pr['response time']
            if rt is None:
                none_count += 1
            else:
                response_times.append(rt)

        # End of for loop: write out last set of aggregate values
        if not first_time_through:
            result_dict['uniweb_number'] = prev_researcher
            if len(response_times) > 0:
                result_dict['mean_response_time'] = mean(response_times)
                result_dict['median_response_time'] = median(response_times)
            result_dict['unreturned_contacts'] = none_count
            aggregated_results.append(result_dict)

        # print('Exiting calculate_aggregate_values')
        return aggregated_results


    def sort_alphabetically(self, results):
        # print('Entering sort_alphabetically')
        for researcher in results:
            researcher_uniweb_number = researcher['uniweb_number']

            uniweb_url = config["UNIWeb"]["host"] + '/professors/' + str(researcher_uniweb_number)
            print(uniweb_url)
            result = requests.get(uniweb_url, verify=False)
            jsonResult = json.loads(result.content.decode('utf-8'))
            if jsonResult and 'membership_information' in jsonResult:
                membership_information = jsonResult['membership_information']
                researcher['last_name'] = membership_information['last_name']
                researcher['first_name'] = membership_information['first_name']
                # print('researcher')
                # print(researcher)
            else:
                print('researcher_uniweb_number')
                print(researcher_uniweb_number)
                print('jsonResult')
                print(jsonResult)

        # print('Exiting sort_alphabetically')
        return sorted(results, key=itemgetter('last_name', 'first_name'))

    def final_cleanup(self, results):
        # print('Entering final_cleanup')
        clean_results = []
        for researcher in results:
            result_dict = {}
            # result_dict['researcher_uniweb_number'] = researcher['researcher_uniweb_number']
            result_dict['last_name'] = researcher['last_name']
            result_dict['first_name'] = researcher['first_name']

            try:
                result_dict['mean_response_time'] = researcher['mean_response_time']
            except KeyError:
                result_dict['mean_response_time'] = ""

            try:
                result_dict['median_response_time'] = researcher['median_response_time']
            except KeyError:
                result_dict['median_response_time'] = ""

            try:
                result_dict['unreturned_initial_contacts'] = researcher['unreturned_contacts']
            except KeyError:
                result_dict['unreturned_initial_contacts'] = ""

            clean_results.append(result_dict)

        # print('Exiting final_cleanup')
        return clean_results

# Instantiated once when the odin app loads rather than on every call.
reports_supervisors = Model()
