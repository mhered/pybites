import csv
from collections import Counter

import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""

    with requests.Session() as s:
        data = s.get(CSV_URL)

    return data.content.decode('utf-8')
    

def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    lst = list(csv.reader(content.splitlines(), delimiter=','))
    
    count = Counter([row[2] for row in lst[1:]])
    
    for timezone in sorted(count.keys()):
        print(f"{timezone:20s}| "+ "+"*count[timezone])

# create_user_bar_chart(get_csv())