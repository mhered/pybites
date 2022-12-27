from pprint import pprint
from itertools import islice
from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    special_date = PYBITES_BORN
    while True:
        special_date+=timedelta(days=100)
        yield special_date
gen = gen_special_pybites_dates()
pprint(list(islice(gen, 5)))