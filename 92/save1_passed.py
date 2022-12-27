from collections import namedtuple
from datetime import datetime, timedelta
import bisect

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', 1),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    
    if not isinstance(date, datetime) or date > NOW:
        raise ValueError
        
    offset= NOW - date
    secs = offset.total_seconds()

    idx = bisect.bisect([item.offset for item in TIME_OFFSETS], secs)
    if idx>=len(TIME_OFFSETS):
        return date.strftime('%m/%d/%y')
    result = TIME_OFFSETS[idx]
    return result.date_str.format(round(secs/result.divider)) if result.divider else result.date_str
    

test = [
    (NOW - timedelta(seconds=2), 'just now'),
    (NOW - timedelta(seconds=9), 'just now'),
    (NOW - timedelta(seconds=10), '10 seconds ago'),
    (NOW - timedelta(seconds=59), '59 seconds ago'),
    (NOW - timedelta(minutes=1), 'a minute ago'),
    (NOW - timedelta(minutes=1, seconds=40), 'a minute ago'),
    (NOW - timedelta(minutes=2), '2 minutes ago'),
    (NOW - timedelta(minutes=59), '59 minutes ago'),
    (NOW - timedelta(hours=1), 'an hour ago'),
    (NOW - timedelta(hours=2), '2 hours ago'),
    (NOW - timedelta(hours=23), '23 hours ago'),
    (NOW - timedelta(hours=24), 'yesterday'),
    (NOW - timedelta(hours=47), 'yesterday'),
    (NOW - timedelta(days=1), 'yesterday'),
    (NOW - timedelta(days=2), '05/19/18'),
    (NOW - timedelta(days=7), '05/14/18'),
    (NOW - timedelta(days=100), '02/10/18'),
    (NOW - timedelta(days=365), '05/21/17')
    ]
    
for item in test:
    print(pretty_date(item[0]))