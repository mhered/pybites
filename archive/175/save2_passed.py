import datetime

def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    start, end = min(dates), max(dates)
    
    all_dates_in_range = [start + datetime.timedelta(days=x) for x in range((end-start).days)]
    
    return [date for date in all_dates_in_range if date not in dates]
    
