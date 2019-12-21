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
    length = len(words)
    if length > 0:
        v /= length
    return v


file_path = r'C:\dhj-learning\研一课程\自然语言处理\NLP-project\word2vec\question_vector_s.txt'
# 把文件按行读取进入texts列表，列表元素为行
vectors = np.loadtxt(file_path)

text_to_predict = input("Enter your question: ").lower()
text_vector = get_sentence_vector(text_to_predict)
print("begin compute:Now time is ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
i = -1
a = []
for vector in vectors:
    i = i + 1
    norm_now = norm(text_vector) * norm(vector)
    if norm_now > 0:
        similarity =np.dot(text_vector, vector) / norm_now
    else:
        similarity = 0
    # a.append(similarity)
    if similarity > 0.95:
        # break
        print(i + 1, "-th sentence, similarity is", similarity)
print("emd compute:Now time is ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# print("similarity:", a)
