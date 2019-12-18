from SOUGOU import test as SOUGOUtest
from question_classifier import classify

from AnswerExtractor import AE1,AE2,AE3,AE4,AE5,AE6
from spelling_corrector import spell
from get_answers import get_best_answer_on_url


question_definition = {
    1: "how to do sth",
    2: "yes or no",
    3: "why",
    4: "campare",
    5: "what, definition",
    6: "others"
}

def assemble(results):
    print('************************************************')
    k = results[0]
    for e in results:
        print(e)
        if k[0] < e[0]:
            k = e
    print('************************************************')
    return k[1]


def QA_entry(question):
    """
        This is the entry of the QA system
    """
    
    print('\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"')
    question = spell(question)
    print('<<<classifying...>>>')
    Q_type = classify(question)
    print('question type is {}. {}'.format(Q_type, question_definition[Q_type]))

    print('\n')
    print('<<<SOUGOU processing...>>>')
    SOUGOU_res = SOUGOUtest(question)

    answer_link = 'https://stackoverflow.com/questions/10601304/how-to-declare-and-close-inputsteam'

    response = get_best_answer_on_url(answer_link)
    assert(response[0] == "Accept answer")
    answer_raw = response[1][1]
    print('raw answer: {}'.format(answer_raw))

    print('<<<AE1 is processing...>>>')
    R1 = AE1.answer(question, Q_type, answer_raw)
    print('\n')

    print('<<<AE2 is processing...>>>')
    R2 = AE2.answer(question, Q_type)
    print('\n')

    R3 = AE3.answer(question, Q_type)
    R4 = AE4.answer(question, Q_type)
    R5 = AE5.answer(question, Q_type)
    R6 = AE6.answer(question, Q_type)

    print('<<<assembling...>>>')
    answer = assemble([[0.5, SOUGOU_res],R1,R2,R3,R4,R5,R6])
    print('\n')

    return answer

if __name__ == "__main__":
    print(QA_entry('how to declare and close InputSteam?'))
