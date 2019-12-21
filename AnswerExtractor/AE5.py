#############################################
# Type 5: xxx
# xxx
#############################################

def answer(question, Q_type=5, answer_raw=''):
    """
    Input :
        question: string
        Q_type: integer
    Outout:
        percentage: 0 or 1, may range from [0, 1] latter.
            (this feature is designed for function 'assemble' in 'QA_system.py')
        answer: string
    """
    
    if Q_type != 5:
        return [0, '']
    percentage = 0
    return [percentage, answer_raw]

