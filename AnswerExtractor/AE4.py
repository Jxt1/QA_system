#############################################
# Type x: 
# xxx
#############################################

def answer(question, Q_type=6, answer_raw=''):
    """
    Input :
        question: string
        Q_type: integer
    Outout:
        percentage: 0 or 1, may range from [0, 1] latter.
            (this feature is designed for function 'assemble' in 'QA_system.py')
        answer: string
    """
    
    ############################################
    # TODO
    ############################################

    if Q_type != 4:
        return [0, '']
    percentage = 1

    return [percentage, '\n'.join(answer_raw)]

