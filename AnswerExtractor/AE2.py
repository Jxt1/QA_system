#############################################
# Type 2: yes or no
# zf
#############################################

import re
import get_answers

def answer(question, Q_type=2, answer_raw=''):
    """
    Input :
        question: string
        Q_type: integer
    Outout:
        percentage: 0 or 1, may range from [0, 1] latter.
            (this feature is designed for function 'assemble' in 'QA_system.py')
        answer: string
    """
    
    if Q_type != 2 or answer_raw == '':
        return [0, '']
    print(answer_raw)
    
    percentage = 1
    answer_list = handle_yes_or_no(answer_raw)
    answer = ''.join(answer_list)
    answer = answer.replace('$code$', '')
    return [percentage, answer]


# 根据URL获取答案
def Hyon(question_url):
    i = 0
    while i < 3:
        request = get_answers.get_best_answer_on_url(question_url)
        if request != 'Access error': 
            break
        i = i + 1
    
    if request == 'Access error':
        return 'Network error, couldn\'t answer this question!'
    elif request == 'No answer':
        return 'This question cannot be answered!'
    else:
        vote, answer, comments = request[1]
        return handle_yes_or_no(answer)
    
# 输入：原始答案(list)
# 输出：答案(list)
def handle_yes_or_no(ans):
    for item in ans:
        if re.match('No[.,; ]', item):
            return 'No'
        elif re.match('Yes[.,; ]', item):
            return ans
    ans.insert(0, 'Yes. ')
    return ans

if __name__ == "__main__":   
    print(Hyon('https://stackoverflow.com/questions/244777/can-comments-be-used-in-json'))
    print(Hyon('https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method'))
    print(Hyon('https://stackoverflow.com/questions/588004/is-floating-point-math-broken'))

