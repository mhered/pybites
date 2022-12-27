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
    for zone in timezones:
        if zone not in TIMEZONES:
            raise ValueError
        if not (6 <= utc.astimezone(pytz.timezone(zone)).hour <= 22):
            return False
    return True
