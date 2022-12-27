from datetime import date
import dateutil.relativedelta as rd


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    start=date(year=year, month=4, day=30)
    return start+rd.relativedelta(days=+1, weekday=rd.SU(+2))
    
for year in range(2018,2028,1):
    print(get_mothers_day_date(year))
