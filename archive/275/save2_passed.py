from collections import Counter

import bs4
import requests
import re


COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}

def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""

    CONTENT = requests.get(COMMON_DOMAINS).text

    soup = bs4.BeautifulSoup(CONTENT, "html.parser")
    target_div=soup.find(attrs=TARGET_DIV)
    row_domains=target_div.find_all('tr')
    return [row.td.next_sibling.next_sibling.get_text() for row in row_domains ]

def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()

    # your code
    domains = []
    for email in emails:
        domain = re.split('@',email)[1]
        if domain not in common_domains:
            domains.append(domain) 
    return Counter(domains).most_common()

    
lst= get_common_domains()
print(len(lst))
print(lst)

test_emails="""
ssainsberry0@bbb.org
d.crauford1@gmail.com
nmaccawley2@zdnet.com
gsteinor3@vkontakte.ru
nmayer4@zdnet.com
llohrensen5@bbb.org
trich6@jigsy.com
mbiggs7@linkedin.com
rjaquest8@gmail.com
edimitresco9@zdnet.com
rvaraha@yahoo.com
""".strip().split()
print(get_most_common_domains(test_emails))
