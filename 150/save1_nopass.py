import json
import re
from pprint import pprint

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""


def convert_to_json(members=members):
    
    lst=[]
    for i,line in enumerate(members.lstrip().splitlines()):
        words = re.split('[,;|]',line)
        if i==0:
            headers=words
        else:
            item=dict((key,value) for key, value in zip(headers,words))
            lst.append(item)
    
    return lst

pprint(convert_to_json())