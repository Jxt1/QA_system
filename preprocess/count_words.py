from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
import json


def func_dict(word_list):
    count_dict = {}
    for item in word_list:
        if item not in ENGLISH_STOP_WORDS:
            count_dict[item] = count_dict[item] + 1 if item in count_dict else 1
    return sorted(count_dict.items(), key=lambda x: x[1], reverse=True)


question_path = 'data\\question.txt'
count_words_path = 'data\\dict_of_count.json'
with open(question_path, encoding='UTF-8') as file:
    texts = file.read().split()
    dict = func_dict(texts)

with open(count_words_path, 'w') as file:
    json.dump(dict, file)

