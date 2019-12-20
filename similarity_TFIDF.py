"""an easy solution using sklearn and it's going to work fine.
1. Use tfidfvectorizer to get a vector representation of each text
2. Fit the vectorizer with your data, removing stop-words(generally the most common words)
3. Transform the new entry with the vectorizer previously trained
4. Compute the cosine similarity between this representation and
each representation of the elements in your data set.
TODO  5. If you have a hugh dataset you can cluster it (for example
using KMeans from scikit learn) after obtaining the representation,
and before predicting on new data."""

from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cluster import KMeans
# from sklearn.metrics import adjusted_rand_score
import numpy as np
from scipy.linalg import norm

question_path = r'data\\question.txt'
vectorizer = TfidfVectorizer(stop_words="english", min_df=5)
question_TFIDF_array = []


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


def TFIDF_similarity(question_str):
    input_sentence_vector = vectorizer.transform([question_str]).toarray()
    Y = input_sentence_vector
    # print('input vector',input_sentence_vector)
    print('computing simirity')
    similarity = 0
    i = -1
    for x in question_TFIDF_array:
        i = i + 1
        t_norm = norm(x.toarray()) * norm(Y[0])
        if t_norm > 0:
            temp = np.dot(x.toarray(), Y[0]) / t_norm
            # print(temp)
            if temp > 0.7:
                similarity = temp
                break
    return similarity, i


if __name__ == '__main__':
    with open(question_path, 'r', encoding='UTF-8') as question_file:
        question_corpus = question_file.read().splitlines()
        print('begin computing question TFIDF array……')
        question_TFIDF_array = vectorizer.fit_transform(question_corpus)
        print('end computing question TFIDF array')
    #words = vectorizer.get_feature_names()
    #print("words", words)
    #print("words num", len(words))
    text_to_predict = input("Enter your question: ")
    similarity, index = TFIDF_similarity( process_question(text_to_predict))
    print('the max similarity is:', similarity)
    print('the index of sentence is:', index)
