# encoding=utf-8
import nltk


def define_type(s):
    # 定义how关键词类型
    t1 = ['How', 'how']
    for each in t1:
        if each in s:
            return 1
    # 定义yes or no关键词类型
    t2 = ['Can', 'Is there', 'Is', 'Are', 'Does', 'Do']
    for each in t2:
        if each in s:
            return 2
    # 定义why关键词类型
    t3 = ['Why', 'why', 'reason', 'reasoning']
    for each in t3:
        if each in s:
            return 3
    # 定义compare关键词类型
    t4 = ['compare', 'Compare', 'difference', 'differences', 'Difference', 'Differences', 'vs', 'vs.']
    for each in t4:
        if each in s:
            return 4
    # 定义名词解释关键词，'what do ... mean'和'what do ... do'类型的问题
    t5 = ['What do', 'What does', 'what do', 'what does']
    for each in t5:
        if each in s:
            return 5
    # 定义名词回答关键词类型
    t6 = ['what', 'which', 'who', 'where', 'when', 'What', 'Which', 'Who', 'Where', 'When']
    for each in t6:
        if each in s:
            return 6
    # 以动词开始的祈使句归类为how问题
    sent = nltk.sent_tokenize(s.lower())
    word_list = nltk.word_tokenize(sent[0])
    first = [word_list[1]]
    character = nltk.pos_tag(first)
    first_word = character[0][1]
    # print(character)
    if first_word == 'VB' or first_word == 'VBG' or first_word == 'VBD' or first_word == 'VBP' or first_word == 'VBZ' \
            or first_word == 'VBN':
        return 1
    else:
        return 7


def classify(question):
    return define_type(question)

if __name__ == "__main__":
    classify('how to do?')
    pass

