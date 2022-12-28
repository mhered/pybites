import os
import urllib.request
import time
import sys

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'
BOOK_SENT_TO_SLACK="sending to slack channel"
PYTHON = "python"

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)

def create_chart():
    last_date = "00-00"
    with open(SAFARI_LOGS) as f:
        for line in f:
            date, rest = line.split(" ", 1)
            _, book_title = rest.split("-", 1)

            if BOOK_SENT_TO_SLACK in next(f):
                if date != last_date:
                    sys.stdout.write("\n"+date+" ")
                    last_date = date
                sys.stdout.write(PY_BOOK if PYTHON in book_title.lower() else OTHER_BOOK)

                    
create_chart()