# 去特殊标点
"""string.punctuation 库中包含的特殊符号，用以参考
>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
注：很多问题中有中文的 “”
"""


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


#  处理原始文件，得到一个只包含所有问题的纯的question.txt
# TODO 处理原始文件，得到一个map，关键字是label，含有这个关键字的问题的index
file_path = 'data//stackoverflow_index.txt'
question_file_handle = open('data//question.txt', 'w', encoding='utf-8')
# label_file_handle = open('label_index.txt', 'w', encoding='utf-8')

# 把文件按行读取进入texts列表，列表元素为行
with open(file_path, encoding='UTF-8') as file:
    texts = file.read().splitlines()
    # print(texts)
all_question_line = []  # 问题行列表
# 去句首数字
for tmp_str in texts[::4]:
    tmp_list = tmp_str.split()
    all_question_line.append(" ".join(tmp_list[1:]))

for question_str in all_question_line:
    question_file_handle.write(process_question(question_str))
    question_file_handle.write("\n")

question_file_handle.close()
