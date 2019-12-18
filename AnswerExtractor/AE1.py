#############################################
# Type 1: how to do sth
# jxt
#############################################


def out_code(codes):
    print('\n{}\n'.format(codes))


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
        answer.append('{}. '.format(cnt) + e)
        print(e)
        cnt = cnt + 1
    # print(answer_raw)

    return [1, '\n'.join(answer)]


import re


def my_split(str,sep=u"要求\d+|岗位\S+"):  # 分隔符可为多样的正则表达式
    wlist = re.split(sep,str)
    sepword = re.findall(sep,str)
    sepword.insert(0," ") # 开头（或末尾）插入一个空字符串，以保持长度和切割成分相同
    wlist = [ x+y for x,y in zip(wlist,sepword) ] # 顺序可根据需求调换
    return wlist

if __name__ == "__main__":
    inputstr = "岗位：学生： \n要求1.必须好好学习。\n要求2.必须踏实努力。\n要求3.必须求实上进。"
    res = my_split(inputstr)
    print(res)
