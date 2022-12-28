from datetime import date

import dateutil.rrule as RR

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY, N=100):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    
    return list(RR.rrule(freq=RR.DAILY, count=N, dtstart=start_date, byweekday=[RR.MO,RR.TU,RR.WE,RR.TH, RR.FR]))


print(get_hundred_weekdays(start_date=date.today(), N=5))