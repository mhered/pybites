from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime

# prep data
tmp = os.getenv("TMP", "/tmp")
page = "us_holidays.html"
holidays_page = os.path.join(tmp, page)
urlretrieve(f"https://bites-data.s3.us-east-2.amazonaws.com/{page}", holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    result = {}
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table", {"class": "list-table"})
    table_body = table.find("tbody")
    for row in table_body.find_all("tr"):
        holiday_date = row.find("time").get("datetime")
        holiday_month = datetime.strptime(holiday_date, "%Y-%m-%d").strftime("%m")
        holiday_name = row.find("a").text.strip()
        holidays[holiday_month].append(holiday_name)
        # result.setdefault(holiday_month, []).append(holiday_name)
    return holidays
    # return defaultdict(None, result)


# print(get_us_bank_holidays())