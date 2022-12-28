from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> str:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    dt = timedelta()
    for item in delay_time.split():
        if 'd' in item:
            dt+=timedelta(days=int(item.strip('d')))
        elif 'h' in item:
            dt+=timedelta(hours=int(item.strip('h')))
        elif 'm' in item:
            dt+=timedelta(minutes=int(item.strip('m')))
        elif 's' in item:            
            dt+=timedelta(seconds=int(item.strip('s')))
        else:
            dt+=timedelta(seconds=int(item))
        
    return f"{task} @ {datetime.strftime(start_time+dt, '%Y-%m-%d %H:%M:%S')}"       


print(add_todo("11h 10m", "Wash my car"))
print(add_todo("30d", "Code a Bite"))
print(add_todo("5m 3s", "Go to Bed"))