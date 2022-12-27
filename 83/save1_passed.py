#!/usr/bin/env python

from datetime import datetime
from pytz import timezone, utc

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    utc_dt = utc.localize(naive_utc_dt)
    return (utc_dt.astimezone(AUSTRALIA), utc_dt.astimezone(SPAIN))


if __name__ == "__main__":
    print(what_time_lives_pybites(datetime(2018, 11, 1, 14, 10, 0)))
