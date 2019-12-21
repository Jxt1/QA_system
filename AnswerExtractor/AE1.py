#############################################
# Type 1: how to do sth
# jxt
#############################################

def out_code(codes):
    print('\n{}\n'.format(codes))

def check_in(question, answer):
    words = answer.split(' ')
    for word in words:
        if word in question:
            return True
    return False

def answer(question, Q_type, answer_raw):
    """
    Input :
        question: string
        Q_type: integer
    Outout:
        percentage: 0 or 1, may range from [0, 1] latter.
            (this feature is designed for function 'assemble' in 'QA_system.py')
        answer: string
    """

    percentage = 0
    if Q_type != 1:
        return [0, '']

    # print(answer_raw.replace("\\n", "\n"))

    # pattern = r'\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|。|、|；|‘|’|【|】|·|！| |…|（|）'
    pattern = r'.'
    # result_list = re.split(pattern, answer_raw)

    answer = []
    cnt = 1

    for e in answer_raw:
        for sentence in [x for x in e.split('. ') if x != '']:
            sentence = sentence.strip('\n')

            if "$code$" in sentence:
                if cnt == 1:
                    answer.append('{}. '.format(cnt) + sentence)
                elif len(sentence) < 40:
                    sentence = sentence[6:].strip('\n')
                    answer[-1] = answer[-1] + '"{}"'.format(sentence)
                else:
                    answer.append(sentence)
            else:
                if not check_in(question, sentence):
                    continue
                answer.append('{}. '.format(cnt) + sentence)
                cnt = cnt + 1
        # print(e)
    # print(answer_raw)

    return [1, '\n'.join(answer)]

if __name__ == "__main__":
    pass
