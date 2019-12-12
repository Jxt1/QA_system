from SOUGOU import test as SOUGOUtest
from question_classifier import classify

from AnswerExtractor import AE1,AE2,AE3,AE4,AE5,AE6
from spelling_corrector import spell


def assemble(results):
    # TODO assemble
    return results[0][1]


def QA_entry(question):
    """
        This is the entry of the QA system
    """
    
    question = spell(question)
    print('classifying...')
    Q_type = classify(question)

    print('SOUGOU processing...')
    SOUGOU_res = SOUGOUtest(question)

    R1 = AE1.answer(question, Q_type)
    R2 = AE2.answer(question, Q_type)
    R3 = AE3.answer(question, Q_type)
    R4 = AE4.answer(question, Q_type)
    R5 = AE5.answer(question, Q_type)
    R6 = AE6.answer(question, Q_type)

    ########################
    # TODO assemble form
    ########################
    answer = assemble([[0.5, SOUGOU_res],R1,R2,R3,R4,R5,R6])

    return answer
