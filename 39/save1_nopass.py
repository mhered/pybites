from datetime import datetime, timedelta
import os
import re
from typing import List
import urllib.request

# getting the data
COURSE_TIMES = os.path.join(
    os.getenv("TMP", "/tmp"),
    'course_timings'
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/course_timings',
    COURSE_TIMES
)


def get_all_timestamps() -> List[str]:
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as f:
        raw_list = [re.findall("\((.+)\)$", line.lstrip()) for line in f.readlines()]
    return [timestamp[0] for timestamp in raw_list if timestamp]


def calc_total_course_duration(timestamps) -> str:
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    lst = []
    for item in timestamps:
        mm_ss = item.split(":")
        lst.append(timedelta(minutes=int(mm_ss[0]), seconds=int(mm_ss[1])))
    return sum(lst, timedelta())
    

print(calc_total_course_duration(get_all_timestamps()))