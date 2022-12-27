from collections import Counter, namedtuple, defaultdict
import csv
import re

import requests

from pprint import pprint

MARVEL_CSV = 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501

Character = namedtuple('Character', 'pid name sid align sex appearances year')

MALE, FEMALE, AGENDER, GENDERFLUID = 'male characters', 'female characters', 'agender characters', 'genderfluid characters'
VALID_GENDERS = [MALE, FEMALE, AGENDER, GENDERFLUID ]

# csv parsing code provided so this Bite can focus on the parsing

def _get_csv_data():
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode('utf-8')


def load_data():
    """Converts marvel.csv into a sequence of Character namedtuples
       as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        name = re.sub(r'(.*?)\(.*', r'\1', row['name']).strip()
        yield Character(pid=row['page_id'],
                        name=name,
                        sid=row['ID'],
                        align=row['ALIGN'],
                        sex=row['SEX'],
                        appearances=row['APPEARANCES'],
                        year=row['Year'])


characters = list(load_data())


# start coding

def most_popular_characters(characters=characters, top=5):
    """Get the most popular character by number of appearances,
       return top n characters (default 5)
    """
    
    """
    # this works but results differ. Note e.g. Benjamin Grimm appears 
    # several times with the same name, this code adds them all together
    
    char_appears = defaultdict(int)
    for character in characters:
         if character.appearances:
            char_appears[character.name]+= int(character.appearances)

    count = Counter(char_appears).most_common(top)
    return [name for name, appears in count]
    """
    
    # wrote this to mimic results in the tests. Now every line of 'Benjamin Grimm'
    # is considered separately
    
    char_appears= {c.pid: int(c.appearances) for c in characters if c.appearances}
    top_chars_by_pid = Counter(char_appears).most_common(top)
    return [c.name for pid,appears in top_chars_by_pid for c in characters if c.pid ==pid]
        



def max_and_min_years_new_characters(characters=characters):
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv
       characters, or the 'year' attribute of the namedtuple, return a tuple
       of (max_year, min_year)
    """
    new_chars_per_year = defaultdict(int)
    for character in characters:
        if character.year:
            new_chars_per_year[character.year]+=1
    count = Counter(new_chars_per_year).most_common()
    return count[0][0],count[-1][0]



def get_percentage_female_characters(characters=characters):
    """Get the percentage of female characters as percentage of all genders
       over all appearances.
       Ignore characters that don't have gender ('sex' attribue) set
       (in your characters data set you should only have Male, Female,
       Agender and Genderfluid Characters.
       Return the result rounded to 2 digits
    """

    """
    appearances_by_gender = defaultdict(int)
    for character in characters:
        if character.sex.lower() in VALID_GENDERS:
            appearances_by_gender[character.sex.lower()]+=int(character.appearances or 0)
        
        else:
            print(character.sex +" : "+ character.appearances)
        
    total = sum(value for value in appearances_by_gender.values())
    return round(100*appearances_by_gender[FEMALE]/total,2)
    """
    
    chars_by_gender = defaultdict(int)
    for character in characters:
        if character.sex.lower():
            chars_by_gender[character.sex.lower()]+=1

    total = sum(value for key, value in chars_by_gender.items() if key.lower() in VALID_GENDERS)
    return round(100*chars_by_gender[FEMALE]/total,2)
    


print(most_popular_characters(top=10))
print(max_and_min_years_new_characters())
print(get_percentage_female_characters())
