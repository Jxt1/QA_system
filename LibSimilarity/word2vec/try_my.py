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

def vector_similarity(s1, s2):
    def sentence_vector(s):
        s_s = ''.join(c for c in s if c not in string.punctuation + '’‘“”')#去掉标点符号
        full_words = list(s_s.split())
        #  words = [w for w in full_words if not w in ENGLISH_STOP_WORDS]#去掉stop words
        words = full_words
        v = np.zeros(100)
        for word in words:
            v += model[word]
        v /= len(words)
        return v

    v1, v2 = sentence_vector(s1), sentence_vector(s2)
    return np.dot(v1, v2) / (norm(v1) * norm(v2))


file_path = r'C:\dhj-learning\研一课程\自然语言处理\NLP-project\stackoverflow_index.txt'
# 把文件按行读取进入texts列表，列表元素为行
with open(file_path, 'r', encoding='UTF-8') as f:
    texts = f.read().lower().splitlines()
    # print(texts)
# all_question_line#问题行列表
all_question_line = []
for tmp_str in texts[::4]:
    tmp_list = tmp_str.split()
    all_question_line.append(" ".join(tmp_list[1:]))
all_link_line = texts[1::4]  # 链接行列表
all_label_line = texts[2::4]  # 输出标签行列表
all_num_line = texts[3::4]  # 输出赞数行列表

text_to_predict = input("Enter your question: ").lower()
print("begin compute:Now time is ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
i = -1
a = []
for question in all_question_line:
    i = i + 1
    similarity = vector_similarity(text_to_predict, question)
    #a.append(similarity)
    if similarity > 0.95:
        # break
        print(i + 1, "-th sentence, similarity is", similarity)
        print("similar question:", all_question_line[i])
        print(all_link_line[i])
print("emd compute:Now time is ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#print("similarity:", a)

