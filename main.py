from bs4 import BeautifulSoup as Soup
from pathlib import Path
from collections import namedtuple
from datetime import datetime
from dateutil.parser import parse
from pprint import pprint
import re

# import requests
# PROFILE = 'https://codechalleng.es/profiles/mhered8b899449424048c5'
# CONTENT = requests.get(PROFILE).text
# does not work because the table is not in the HTML...
# instead I copied the HTML manually to a local file

p = Path(__file__).with_name('profile.html')
with p.open('r') as f:
    CONTENT = f.read()    

Bite = namedtuple('Bite', 'title platform_link repo_link completed score submits')

def get_bites():
    """make a Soup object, parse the relevant html sections, and return a list of Bite namedtuples"""
    soup = Soup(CONTENT, 'html.parser')
    table = soup.find('table', {'class',"filterList mui-table mui-table--bordered smallerFont"})
    bites = []
    for row in table.find_all('tr')[1:]:
        fields=row.find_all("td")
        title = fields[0].text.strip()
        platform_link = f"https://codechalleng.es{fields[0].a['href']}"
        bite_num = re.findall(r'\d+', fields[0].a['href'])[0]
        repo_link = f'./archive/{bite_num}/'
        completed = parse(fields[1].text)
        score = int(fields[3].text)
        submits = int(fields[4].text)
        bite = Bite(title, platform_link, repo_link, completed, score, submits)
        bites.append(bite)
    return bites

def print_bites(bites):
    longest = max(bites, key = lambda x:len(x.title + x.platform_link))
    longest = len(longest.title + longest.platform_link) + 6
    for bite in bites:
        title = f"[{bite.title}]({bite.platform_link})"
        print(f" | {title:<{longest}s} | [my code]({bite.repo_link:>7}) | {bite.completed.strftime('%d/%m/%Y')} | {bite.score:>2} | {bite.submits:>2} | ")

if __name__ == "__main__":
    bites = get_bites()
    print_bites(bites)

    
