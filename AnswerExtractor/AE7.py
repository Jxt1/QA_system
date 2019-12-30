#############################################
# Type 7: Others
# jxt
#############################################

from ..utils import process_question
from ..get_answers import get_best_answer_on_url

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
    answer = 'Sorry, I cannot solve this question'

    try:
        url = 'https://stackoverflow.com/search?q={}'.format('+'.join(question.split(' ')))
        
        strhtml = requests.get(url)        #Get方式获取网页数据
        soup=BeautifulSoup(str(strhtml.content).encode('utf-8',),'lxml')
        for i, child in enumerate(soup.body.find(id='questions').children):
            if child.find('h3') == -1:
                continue

            link = 'https://stackoverflow.com' + child.h3.a['href']
            answer = get_best_answer_on_url(link)

            break

    except Exception as e:
        print(e)

    return [percentage, answer]

if __name__ == "__main__":
    answer('how to use')

