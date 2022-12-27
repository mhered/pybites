from datetime import datetime

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    earth_duration = PY2_DEATH_DT - start_date
    return round(earth_duration.total_seconds()/3600.0,2)


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    earth_hours = py2_earth_hours_left(start_date)
    miller_mins = round(60*earth_hours/(7*365*24),2)
    return miller_mins

print(py2_earth_hours_left())
print(py2_miller_min_left())