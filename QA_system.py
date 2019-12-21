from SOUGOU import test as SOUGOUtest
from question_classifier import classify

from AnswerExtractor import AE1,AE2,AE3,AE4,AE5,AE6,AE7
from spelling_corrector import spell
from get_answers import get_best_answer_on_url
from similarity_main import similiar
from utils import process_question, ques_str_op

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

    question = ques_str_op(question)

    print('\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"')
    question = spell(question)
    print('<<<classifying...>>>')
    Q_type = classify(question)
    print('question type is {}. {}'.format(Q_type, question_definition[Q_type]))

    print('\n')
    print('<<<SOUGOU processing...>>>')
    # SOUGOU_res = SOUGOUtest(question)

    print('\n')
    print('<<<looking up similar question...>>>')
    answer_link = similiar(process_question(question))
    print('answer link is {}'.format(answer_link))

    response = get_best_answer_on_url(answer_link)
    # assert()
    if response == "Access error":
        answer_raw = ['Sorry, I have some problem in finding an answer']
    elif response[0] == "No answer":
        answer_raw = ['Sorry, I cannot answer the question']
    else:
        answer_raw = response[1][1]

    print('raw answer: {}'.format(answer_raw))

    print('<<<AE1 is processing...>>>')
    R1 = AE1.answer(question, Q_type, answer_raw)
    print('\n')

    print('<<<AE2 is processing...>>>')
    R2 = AE2.answer(question, Q_type, answer_raw)
    print('\n')

    R3 = AE3.answer(question, Q_type)
    R4 = AE4.answer(question, Q_type)
    R5 = AE5.answer(question, Q_type)
    R6 = AE6.answer(question, Q_type)
    R7 = AE7.answer(question, Q_type)

    print('<<<assembling...>>>')
    answer = assemble([R1,R2,R3,R4,R5,R6])
    # answer = assemble([[0.5, SOUGOU_res],R1,R2,R3,R4,R5,R6])
    print('\n')

    return answer

if __name__ == "__main__":
    print(QA_entry('How do I undo \'git add\' before commit?')) # Type 1: how

    # print(QA_entry('how to declare and close InputSteam?')) # Type 1: how

    # print(QA_entry('how to set a timer in Python?')) # Type 1: how (not in db)

    # print(QA_entry('Does Python have a string \'contains\' substring method?')) # Type 2: y/n

