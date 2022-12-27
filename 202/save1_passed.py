import csv
import os
from pathlib import Path
from urllib.request import urlretrieve
import re
from collections import defaultdict, Counter

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
TMP = Path(os.getenv("TMP", "/tmp"))
stats = TMP / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats,encoding="utf-8-sig") as f:
        result=defaultdict(float)
        bites = [(row['Bite'], row['Difficulty']) for row in csv.DictReader(f.read().splitlines(), delimiter=';')]
        for bite, difficulty in bites:
            bite_stripped = re.search('(?<=Bite )[0-9]+(?=\.)', bite)
            if not bite_stripped: # exclude three special PyCon19 bites which use : not . - Difficulty is None anyway 
                # print(bite, difficulty)
                continue
            if difficulty == 'None': # exclude bites with Difficulty None
                continue
            result[bite_stripped[0]]=float(difficulty)
    return [int(item[0]) for item in Counter(result).most_common(N)]  


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)