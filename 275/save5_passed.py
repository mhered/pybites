from collections import Counter

import bs4
import requests


COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}

def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""

    content = requests.get(url).text

    soup = bs4.BeautifulSoup(content, "html.parser")
    target_div=soup.find('div', TARGET_DIV)
    row_domains=target_div.find_all('tr')
    return [row.td.next_sibling.next_sibling.get_text() for row in row_domains ]

def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()

    # your code
    domains = [email.split('@')[1] for email in emails]
    domains_filtered= [domain for domain in domains if domain not in common_domains]

    return Counter(domains_filtered).most_common()


lst= get_common_domains()
print(len(lst))
print(lst)

# sample email list from mockaroo, edited manually
test_emails='''
sally.sainsberry@bbb.org
dcrauford1@gmail.com
nmaccawley2@zdnet.com
gsteinor3@vkontakte.ru
n.mayer4@zdnet.com
laurent.lohrensen5@bbb.org
trich6@jigsy.com
mbiggs7@linkedin.com
raymond.jaquest@gmail.com
edimitresco9@zdnet.com
rvaraha@yahoo.com
'''.strip().split()
print(get_most_common_domains(test_emails))
