from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    label, timestamp, msg = tuple (line.strip().split(" ", maxsplit=2))
    l_date, l_time = tuple(timestamp.split("T", maxsplit=1))
    year, month, day = tuple(l_date.split("-", maxsplit=2))
    hour, minute, second = tuple(l_time.split(":", maxsplit=2))
    return datetime(int(year),int(month),int(day), int(hour),int(minute),int(second))
    

def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_lines=[line for line in loglines.splitlines() if SHUTDOWN_EVENT in line]
    first_shutdown=convert_to_datetime(shutdown_lines[0])
    last_shutdown=convert_to_datetime(shutdown_lines[-1])
    return last_shutdown-first_shutdown


print(convert_to_datetime("       INFO 2014-07-03T23:27:51 supybot Shutdown complete."))


loglines ="""
ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file
INFO 2015-10-03T10:12:51 supybot Shutdown initiated.
INFO 2015-10-03T10:13:51 supybot Shutdown continued.
INFO 2015-10-03T10:22:51 supybot Shutdown continued.
INFO 2015-10-03T11:12:51 supybot Shutdown initiated.
INFO 2016-09-03T02:11:22 supybot Shutdown complete.
"""

print(time_between_shutdowns(loglines))