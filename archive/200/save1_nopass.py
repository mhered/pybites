import os
from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup
import re


TMP = Path(os.getenv("TMP", "/tmp"))
HTML_FILE = TMP / "enchantment_list_pc.html"

# source:
# https://www.digminecraft.com/lists/enchantment_list_pc.php
URL = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "minecraft-enchantment.html")


class Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """
    
    LEVEL={'I':1, 'II':2, 'III':3, 'IV':4 , 'V':5}
    
    def __init__(self, id_name, name, max_level, description, items = None):
        
        self.id_name = id_name  # Internal name of the enchantment
        self.name = name  # User friendly name of the enchantment
        self.max_level = max_level  # Enchantment level. Original is in Roman numerals; they need to be converted to integers
        self.description = description  # Summary of what the enchantment does
        self.items = items or [] # List of item names that are typically enchanted with this enchantment.

    def __repr__(self):
        return f'{self.name.title()} ({self.max_level}): {self.description}'

class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """

    def __init__(self, name, enchantments = None):
        
        self.name = name
        self.enchantments = enchantments or []
        
    def __repr__(self):
        result= f'{self.name.title()}: \n'
        for enchantment in self.enchantments:
            result+=f'  [{enchantment.max_level}] {enchantment.id_name}\n'
        return result


def _get_items(string):
    
    filename=string.split('/')[-1].split('.')[0]
    # replace fishing_rod fishing-rod
    filename=filename.replace('fishing_rod', 'fishing-rod')
    items_raw=filename.split('_')
    items = [item for item in items_raw if item.lower() not in ['enchanted','iron', 'sm']]
    return list(map(lambda x: x.replace('fishing-rod','fishing_rod'),items))

def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
    table = soup.find('table',{'id':'minecraft_items'})
    rows = table.find_all('tr')
    enchantments={}
    for row in rows[1:]:
        # print(row)
        cols = row.find_all('td')
        id_name_raw = cols[0].a['href']
        id_name = re.search('(?<=/enchantments/)[A-Za-z_]+(?=\.php)',id_name_raw).group(0)
        # print(id_name_raw, id_name)
        name = cols[0].a.text
        max_level = Enchantment.LEVEL[cols[1].text.upper()] 
        description = cols[2].text
        items = _get_items(cols[4].find('img',{'class':'img-rounded'})['data-src'])
        enchantments[id_name]=Enchantment(id_name, name, max_level, description,items)
    return enchantments


def _get_item_name(item_id):
    return " ".join(item_id.split('_')).title()


def generate_items(data):
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    items_dict= {}
    
    for enchantment in data.values():
        for item_id in enchantment.items:
            #create Item object with this enchantment or append enchantment if Item exists
            if item_id in items_dict:
                items_dict[item_id].enchantments.append(enchantment)
            else:
                items_dict[item_id] = Item(_get_item_name(item_id),[enchantment])
    
    


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not file.is_file():
            urlretrieve(URL, file)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    print(enchantment_data)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""