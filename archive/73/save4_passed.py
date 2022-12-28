import pytz

MIN_MEETING_HOUR = 6
MAX_MEETING_HOUR = 22
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """
    Receive a utc datetime and one or more timezones and check if
    they are all within MIN_MEETING_HOUR and MAX_MEETING_HOUR
    (both included).
    """
    
    # make naive utc aware
    utc_aware = utc.replace(tzinfo=pytz.utc)
    
    for zone in timezones:
        if zone not in TIMEZONES:
            raise ValueError
        local_time=utc_aware.astimezone(pytz.timezone(zone))
        if not (MIN_MEETING_HOUR <= local_time.hour <= MAX_MEETING_HOUR):
            return False
    return True
