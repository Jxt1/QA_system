import json

count_words_path = 'data\\dict_of_count.json'
word2id_path = 'data\\word2id.json'

word_id_dict = {}
with open(count_words_path, 'r') as file:
    dict = json.load(fp=file)
    i = 0
    for word, count in dict:
        word_id_dict[word] = i
        i = i + 1

with open(word2id_path, 'w') as file:
    json.dump(word_id_dict, file)
