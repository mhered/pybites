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
    
