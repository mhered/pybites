from collections import Counter
from operator import itemgetter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    automakers_in_year = set([item['automaker'] for item in data if item['year'] == year])
    models_per_automaker = [(automaker, len(get_models(automaker, year))) for automaker in automakers_in_year]
    print(models_per_automaker)
    return max(models_per_automaker ,key=itemgetter(1))[0]



def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    filtered_list = [item['model'] for item in data if item['automaker'].lower() == automaker.lower() and item['year'] == year]
    dedup_set = set(filtered_list)
    return dedup_set
    

print(most_prolific_automaker(2000))