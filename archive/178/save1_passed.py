from collections import Counter, defaultdict
import os
from typing import Tuple
from urllib.request import urlretrieve
import re

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(
    commit_log: str = commits,
    year: int = None
) -> Tuple[str, str]:
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    
    result=defaultdict(int)
    
    with open(commit_log) as f:
        lines=f.readlines()
    
    for line in lines:
        """
        print(line)
        """
        date, changes = line.split('|')

        date=parse(date.strip(),ignoretz=True, fuzzy_with_tokens=True)[0]
        
        if year and year!=date.year:
            continue
        key=date.strftime("%Y-%m")

        insertions = re.findall('([0-9]+) insertion',changes) or [0]
        deletions = re.findall('([0-9]+) deletion',changes) or [0]
        """
        print(f'{date.year=} {date.month=} {insertions=} {deletions=}')
        """
        count=int(deletions[0])+int(insertions[0])

        result[key]+=count
        
        """
        print(f'{key=} {count=}')
        """
        
    sorted_count = Counter(result).most_common()
    """
    print(sorted_count)
    """
    return sorted_count[-1][0],sorted_count[0][0]
    
print(get_min_max_amount_of_commits(commits,2019))
    