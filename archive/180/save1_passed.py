from collections import defaultdict
from pprint import pprint 

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    # your code
    for line in data.splitlines():
        surname, name, country = tuple(line.split(","))
        if country != "country_code":
            countries[country].append(" ".join([name,surname]))
    return countries
    
pprint(group_names_by_country())