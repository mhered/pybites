from datetime import datetime, timedelta, date

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract unique dates from DB table representation as shown in Bite"""
    lines=data.strip().splitlines()
    result=[]
    for line in lines[3:-1]:
        _,date_str,*_=line.split('|')
        date_obj=datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
        result.append(date_obj)
    return sorted(list(set(result)), reverse=True)


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    dates.insert(0, TODAY)
    intervals= [(dates[n-1]-dates[n]).days for n in range(1,len(dates))]
    streak_breaks= list(filter(lambda i: i> 1, intervals)
    if streak_breaks:
        return streak_breaks[0]
    else:
        return len(intervals)
    

    print(dates)
    print(intervals)
    

data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
"""

dates=extract_dates(data)
print(dates)
print(calculate_streak(dates))
