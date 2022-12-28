import os
import urllib.request
import re
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)

def get_words(file):
    with open(file) as f:  
        words = f.read().split()
    return [re.sub(r'[^a-z0-9 ]+', '', word.lower()) for word in words]

def get_harry_most_common_word():
    words = get_words(harry_text)
    stop_words = get_words(stopwords_file)
    lst = [word for word in words if len(word)>0 and word not in stop_words]
    return Counter(lst).most_common(1)
    
    
print(harry_text)
print(get_harry_most_common_word())