from datetime import datetime, timedelta
import calendar
from sqlalchemy import *
from data.models.utils.postgres_mixin import PGModel

class Model(PGModel):

    def __init__(self, *args, **kwargs):
        PGModel.__init__(self, args, kwargs)
        self.students_table = Table('students', self.metadata, autoload=True)

    def get(self, start, end):
        self.connection = self.db_engine.connect()

        start_date = datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.strptime(end, '%Y-%m-%d') + timedelta(days=1)
        create_date = self.students_table.c.date_created

        stmt = select([func.date_trunc('month', create_date).label("month"),\
                        func.count().label("profile_count")]).\
                where(create_date >= start_date).\
                where(create_date < end_date).\
                group_by(func.date_trunc('month', create_date))

        try:
            results = self.connection.execute(stmt).fetchall()
        finally:
            self.connection.close()

        results = [dict(r) for r in results]
        # return results

        # Code from http://stackoverflow.com/questions/34898525/generate-list-of-months-between-interval-in-python/34899127
        # Had previous tried solutions requiring xrange but we don't have that function in our version of Python.
        months_str = calendar.month_name
        months = []
        month_dict = {}
        while start_date < end_date:
            month = start_date.month
            year  = start_date.year
            month_str = months_str[month][0:3]

            month_dict = {
                'month': "{0}-{1}".format(month_str,str(year)[-2:]),
                'profile_count': 0
            }
            months.append(month_dict)
            next_month = month+1 if month != 12 else 1
            next_year = year + 1 if next_month == 1 else year
            start_date = start_date.replace( month = next_month, year= next_year)

        # Now merge them together
        for result in results:
            for month in months:
                if datetime.strftime(result["month"], '%b-%y') == month["month"]:
                    month["profile_count"] = result["profile_count"]
                    break

        return months
        # return results

# Instantiated once when the odin app loads rather than on every call.
reports_profiles_by_month = Model()
