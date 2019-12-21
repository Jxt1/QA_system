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

    flag = False
    for e in answer_raw:
        if "$code$" in e:
            e.replace("$code$", "$code$\n")
            if len(e) < 40:
                e = e.strip("$code$").strip('\n')
                answer[-1] = answer[-1] + e
                flag = True
            elif cnt == 1:
                if flag:
                    answer[-1] = answer[-1] + e
                else:
                    answer.append('{}. '.format(cnt) + e)
                flag = False
            else:
                if flag:
                    answer[-1] = answer[-1] + e
                else:
                    answer.append(e)
                flag = False
        else:
            if flag:
                answer[-1] = answer[-1] + e
            else:
                answer.append('{}. '.format(cnt) + e)
                cnt = cnt + 1
            flag = False
        # print(e)
    # print(answer_raw)

    return [1, '\n'.join(answer)]

if __name__ == "__main__":
    pass
