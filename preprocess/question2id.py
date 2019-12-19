"""
list内置sort的排序结果：可用
>>> e = [[4,6,8,9],[2,4,6,8],[2,3,4,8]]
>>> e.sort()
>>> e
[[2, 3, 4, 8], [2, 4, 6, 8], [4, 6, 8, 9]]
>>> f = [[4,6,8,9,'0'],[2,4,6,8,'1'],[2,3,4,8,'2']]
>>> f.sort()
>>> f
[[2, 3, 4, 8, '2'], [2, 4, 6, 8, '1'], [4, 6, 8, 9, '0']]

本程序把所有question变为其词的id数组（除最后一位外），且每个数组的最后一位标识了此问题在所有
问题中的顺序（从0开始），便于索引其链接
"""


from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
import json

# def question2id(question_str, dict)


question_path = 'data\\question.txt'
word2id_path = 'data\\word2id_new.json'
listofsentence_path = 'data\\listofsentence_new.json'
with open(question_path, 'r', encoding='UTF-8') as question_file:
    texts = question_file.read().splitlines()
    with open(word2id_path, 'r') as word2id_file:
        dict = json.load(fp=word2id_file)
        listofsentence = [[] for index in range(len(texts))]
        i = 0
        for sentence in texts:
            for word in sentence.split():
                if word not in ENGLISH_STOP_WORDS:
                    listofsentence[i].append(dict[word])
            listofsentence[i].sort()
            listofsentence[i].append(i)
            i = i + 1
        listofsentence.sort()
        #print(listofsentence[-1])
        with open(listofsentence_path, 'w') as listofsentence_file:
            json.dump(listofsentence, listofsentence_file)
