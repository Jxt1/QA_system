from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import linecache

# import distance

file_path = r'C:\dhj-learning\研一课程\自然语言处理\NLP-project\stackoverflow_index.txt'

# get linenumbers
count = -1
for count, line in enumerate(open(file_path, 'rb')):
    pass
count += 1

my_question = list(input("Enter your question: ").split())

"""
def edit_distance(s1, s2):
    return distance.levenshtein(s1, s2)
"""


def jaccard_similarity(s1, s2):
    def add_space(s):
        return ' '.join(s)

    # 将字中间加入空格
    s1, s2 = add_space(now_line), add_space(my_question)
    # 转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 求交集
    numerator = np.sum(np.min(vectors, axis=0))
    # 求并集
    denominator = np.sum(np.max(vectors, axis=0))
    # 计算杰卡德系数
    return 1.0 * numerator / denominator


number = []
context = []
for line_number in range(count):
    if line_number % 4 == 0:
        # print(line_number+1)
        get_line = list(linecache.getline(file_path, line_number + 1).split())
        # print(get_line)
        now_line = get_line[1:]
        # print(now_line)
        # print(my_question)
        temp_i = jaccard_similarity(my_question, now_line)
        number.append(temp_i)
        context.append([temp_i, line_number + 1, ' '.join(now_line)])

        # print(edit_distance(my_question, now_line))
temp_ii = number.index(max(number))
print(temp_ii)
print(context[temp_ii])

sort_number = sorted(range(len(number)), key=lambda i:number[i])
print(sort_number[-2])
print(context[sort_number[-2]])
print(sort_number[-3])
print(context[sort_number[-3]])
print(sort_number[-4])
print(context[sort_number[-4]])
