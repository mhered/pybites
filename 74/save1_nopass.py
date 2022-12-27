import calendar
import datetime


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    print(calendar.weekday(date.year,date.month,date.day))

date = datetime.datetime(year=1975,month=4,day=9)
weekday_of_birth_date(date)