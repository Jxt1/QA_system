#############################################
# Type 7: Others
# jxt
#############################################

import sys
sys.path.append('..')

import requests
from bs4 import BeautifulSoup
import pickle
from get_answers import get_best_answer_on_url
from utils import process_question

def answer(question, Q_type=7):
    """
    Input :
        question: string
        Q_type: integer
    Outout:
        percentage: 0 or 1, may range from [0, 1] latter.
            (this feature is designed for function 'assemble' in 'QA_system.py')
        answer: string
    """

    if Q_type != 7:
        return [0.2, '']
    
    question = process_question(question)
        
    percentage = 1

    try:
        url = 'https://stackoverflow.com/search?q={}'.format('+'.join(question.split(' ')))
        print(url)
        
        strhtml = requests.get(url)        #Get方式获取网页数据
        
        soup=BeautifulSoup(str(strhtml.content).encode('utf-8',),'lxml')
        child = soup.find('div', {'class' : 'question-summary search-result'})

        link = 'https://stackoverflow.com' + child.h3.a['href']
        print(link)
        answer = get_best_answer_on_url(link)
        # print(answer)

    except Exception as e:
        print(e)

    return [percentage, 'Sorry, I cannot solve this question.\n\n\n' + answer]

if __name__ == "__main__":
    answer('how to use')

