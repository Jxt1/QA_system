"""
TODO
1、question处理（标点与特殊符号的处理） ==> process_question.py ok
2、统计所有（去掉重用词外）词及其词频（用dictory处理） ==> count_word.py  ok
3、给每个词定义一个id（与词频有关） ==> word2id.py   ok
4、每个句子成为一个sorted list，list最后一位以字符串形式保存句子的原序号      ====> question2id.py ok
5、所有句子append成一个大list（类似二维向量从左到右递增，从上到下递增）其对应的    ===> question_sort.py    ok
问题序号也append成一个对应的list
[[……],
……
[……]]
//
6、对用户输入的问题，转换成list（这一步也要求有个dictory文件） ===>sim_main.py ok
7、查找（相似的词数超过输入句子的一多半 2/3 时输出，可能会输出多条）


a b c
0 1 2

a b: 0 1
b c :2 3

d = dict()
cnt = 0
for word in words:
    d[word] = cnt
    cnt = cnt + 1

print d["char"]
"""
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
import json

word2id_path = 'data\\word2id.json'
listofsentence_path = 'data\\listofsentence.json'
# questionlink_path = 'data\\question_link.txt'
word2id_dict = {}
listofsentence = []  # 问题集合排序句子的id list


# questionlink = []#问题链接集合


def process_question(question_str):
    tmp = list(question_str.lower())
    i = 0
    for c in tmp:
        if c in '“”\'?"':  # 删掉符号
            tmp[i] = ""
        if c in '!&%*=<>^@':  # 符号前后加空格
            tmp[i] = " " + c + " "
        if c in '$(),./:;[\\]_-`{|}~':  # 符号变空格
            tmp[i] = " "
        i = i + 1
    return ''.join(tmp)


def get_similarity(sentence_str):
    list_of_input_sentence = []
    for word in sentence_str.split():
        if word not in ENGLISH_STOP_WORDS:
            try:
                list_of_input_sentence.append(word2id_dict[word])
            except NameError or KeyError:
                list_of_input_sentence.append(len(listofsentence) + 1)

    list_of_input_sentence.sort()
    print(list_of_input_sentence)
    # TODO 在 listofsentence 中找到与list_of_input_sentence最相似的向量，并输出相似度以及index
    print('TODO 在 listofsentence 中找到与list_of_input_sentence最相似的向量(假设是第10个)，并输出相似度以及index')
    similarity = 0
    index = 0

    # index = listofsentence[10][-1]
    print("此时 index = listofsentence[10][-1]")
    return similarity, index


if __name__ == '__main__':
    with open(word2id_path, 'r', encoding='utf-8') as word2id_file:
        print("begin loading word2id dict……")
        word2id_dict = json.load(fp=word2id_file)
        print("end loading word2id dict")
    with open(listofsentence_path, 'r', encoding='utf-8') as listofsentence_file:
        print("begin loading listofsentence.json……")
        listofsentence = json.load(fp=listofsentence_file)
        print("end loading listofsentence.json")

    text_to_predict = input("Enter your question: ")
    similarity, i = get_similarity(process_question(text_to_predict))
    print('the max similarity is:', similarity)
    print('the index of sentence is:', i)
