import os
from pathlib import Path
from urllib.request import urlretrieve

import xml.etree.ElementTree as ET
from collections import defaultdict

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    result = defaultdict(list)

    for country in ET.parse(xml).getroot():
        name = country.find('{http://www.worldbank.org}name').text
        income = country.find('{http://www.worldbank.org}incomeLevel').text
        result[income].append(name) 

    return result
    