from datetime import date

import dateutil.rrule as RR

TODAY = date(year=2018, month=11, day=29)
WEEKDAYS=[RR.MO,RR.TU,RR.WE,RR.TH, RR.FR]

def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    
    return [d.date() for d in RR.rrule(freq=RR.DAILY, count=100, dtstart=start_date, byweekday=WEEKDAYS)]


print(get_hundred_weekdays(start_date=date.today()))