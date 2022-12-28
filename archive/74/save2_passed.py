import calendar
import datetime
WEEKDAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    weekday_index = calendar.weekday(date.year,date.month,date.day)
    return WEEKDAYS[weekday_index]

if __name__ =="__main__":
    date = datetime.datetime(year=2022,month=1,day=1)
    print(weekday_of_birth_date(date))