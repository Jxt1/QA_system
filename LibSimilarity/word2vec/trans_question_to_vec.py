import gensim
import numpy as np
from scipy.linalg import norm
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
import datetime
import string

print("begin load model:Now time is ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# Load Google's pre-trained Word2Vec model.
model = gensim.models.KeyedVectors.load_word2vec_format('my_train_model.txt', binary=False)
print("end load model:Now time is ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def get_sentence_vector(s):
    s_s = ''.join(c for c in s if c not in string.punctuation + '’‘“”')  # 去掉标点符号
    full_words = list(s_s.split())
    words = [w for w in full_words if not w in ENGLISH_STOP_WORDS]  # 去掉stop words
    # words = full_words
    v = np.zeros(300)
    for word in words:
        try:
            v += model[word]
        except KeyError:
            continue
    l = len(words)
    if l > 0:
        v /= l
    return v


file_path = r'C:\dhj-learning\研一课程\自然语言处理\NLP-project\word2vec\question.txt'
file_handle = open('question_vector.txt', 'w', encoding='utf-8')
# 把文件按行读取进入texts列表，列表元素为行
with open(file_path, 'r', encoding='UTF-8') as f:
    texts = f.read().lower().splitlines()

for question in texts:
    vector = get_sentence_vector(question)
    for tmp in vector:
        file_handle.write(str(tmp))
        file_handle.write(" ")
    file_handle.write("\n")
