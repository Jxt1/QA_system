
def define_type(s):
    # 定义how关键词类型
    t1 = ['How', 'What do', 'What does']
    for each in t1:
        if each in s:
            return 1
    # 定义yes or no关键词类型
    t2 = ['Can', 'Is there', 'Is', 'Does', 'Do']
    for each in t2:
        if each in s:
            return 2
    # 定义why关键词类型
    t3 = ['Why', 'reason', 'reasoning']
    for each in t3:
        if each in s:
            return 3
    # 定义compare关键词类型
    t4 = ['compare', 'difference', 'differences', 'Difference', 'Differences', 'vs', 'vs.']
    for each in t4:
        if each in s:
            return 4
    # 定义名词回答关键词类型
    t5 = ['what', 'which', 'who', 'where', 'when', 'What', 'Which', 'Who', 'Where', 'When']
    for each in t5:
        if each in s:
            return 5
    # other可以归类为how问题?
    return 6


def classify(question):

    return define_type(question)
    
