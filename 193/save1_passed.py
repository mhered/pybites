import requests
from bs4 import BeautifulSoup
from collections import namedtuple
from pprint import pprint


cached_so_url = 'https://bites-data.s3.us-east-2.amazonaws.com/so_python.html'

Question = namedtuple('Question', 'question votes views')

def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    CONTENT = requests.get(url).text
    soup = BeautifulSoup(CONTENT, 'html.parser')
    
    
    list_questions = soup.find_all("div", class_="question-summary")

    result = []
    
    for q in list_questions:
        question = q.find('a', {'class': 'question-hyperlink'}).text
        votes = int(q.find('span', {'class': 'vote-count-post'}).text)
        views = q.find('div', {'class': 'views'}).text.strip()
        result.append(Question(question=question,
                votes=votes,
                views=views,
                ))
    
    filtered = [(q.question, q.votes) for q in result if 'm' in q.views]
    return sorted(filtered, key=lambda x:x[1], reverse=True)
    
pprint(top_python_questions())
