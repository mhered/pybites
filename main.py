from bs4 import BeautifulSoup as Soup
from collections import namedtuple, defaultdict
from datetime import datetime
from dateutil.parser import parse
import re
import plotext as plt
from itertools import accumulate

# import requests
# PROFILE = 'https://codechalleng.es/profiles/mhered8b899449424048c5'
# CONTENT = requests.get(PROFILE).text
# does not work because the table is not present in the HTML...
# instead I copied the HTML manually to a local file profile.html

with open('profile.html') as f:
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

def print_markdown_table_of(bites):
    """receives a list of Bite namedtuples and prints in stdout a rows of a formatted as Markdown ready to paste in the README.md"""
    longest = max(bites, key = lambda x:len(x.title + x.platform_link))
    longest = len(longest.title + longest.platform_link) + 6
    for bite in bites:
        title = f"[{bite.title}]({bite.platform_link})"
        print(f" | {title:<{longest}s} | [my code]({bite.repo_link:>7}) | {bite.completed.strftime('%d/%m/%Y')} | {bite.score:>2} | {bite.submits:>2} | ")


def plot_graph_of(bites):
    """receives a list of Bite namedtuples and plots a daily graph of bites completed and points gained (accumulated) since the start"""
    bites = sorted(bites, key = lambda x:x.completed)
    points=defaultdict(int)
    bites_count=defaultdict(int)
    start = min([bite.completed for bite in bites])
    for bite in bites:
        label = bite.completed - start
        points[label.days+1]+=bite.score
        bites_count[label.days+1]+=1 
    
    days = list(points.keys())

    points=list(accumulate(points.values()))
    bites_count=list(accumulate(bites_count.values()))

    plt.plot(days,points, label='Points')
    plt.plot(days,bites_count, label='Bites')  
    plt.title("100 Days Of Code Daily Progress") # to apply a title
    plt.grid(1, 1)       # to add grid lines
    plt.xlabel("days")
    plt.show() # to finally plot

    # this script calculates correctly the number of points (619)
    # the platform does not count newbie bites but this script does count them  
    # (the difference between 246 vs 233 in the platform is the 13 newbie bites)
    # the script finds 90 days with bites, i.e. 10 days with no bites completed
    # in the platform there are only 3 days with no bites completed
    # could be an issue of naive datetime?

if __name__ == "__main__":
    bites = get_bites()
    # print_markdown_table_of(bites)
    plot_graph_of(bites)

    
