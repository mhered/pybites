import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    lst=[]
    for elem in ET.fromstring(content)[0]:
        if elem.tag == 'item':
            for attrb in elem:
                if attrb.tag == 'category':
                    lst.append(attrb.text)
    return Counter(lst).most_common(n)

print(get_pybites_top_tags(10))