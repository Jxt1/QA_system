#############################################
# Type 6: Others
# jxt
#############################################

def answer(question, Q_type=6):
    """
    Input :
        question: string
        Q_type: integer
    Outout:
        percentage: 0 or 1, may range from [0, 1] latter.
            (this feature is designed for function 'assemble' in 'QA_system.py')
        answer: string
    """
    
    if Q_type != 6:
        return [0.2, '']
    percentage = 1
    answer = 'Sorry, I cannot solve this question'

    return [percentage, answer]

