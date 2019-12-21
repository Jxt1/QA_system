#  处理原始文件，得到一个只包含所有问题的纯的question.txt
# TODO 处理原始文件，得到一个map，关键字是label，含有这个关键字的问题的index
import string

file_path = r'C:\dhj-learning\研一课程\自然语言处理\NLP-project\stackoverflow_index.txt'
question_file_handle = open('question.txt', 'w', encoding='utf-8')
# label_file_handle = open('label_index.txt', 'w', encoding='utf-8')

# 把文件按行读取进入texts列表，列表元素为行
with open(file_path, encoding='UTF-8') as file:
    texts = file.read().lower().splitlines()
    # print(texts)
all_question_line = []  # 问题行列表
# 去句首数字
for tmp_str in texts[::4]:
    tmp_list = tmp_str.split()
    all_question_line.append(" ".join(tmp_list[1:]))
# 去特殊标点

for question_str in all_question_line:
    tmp = list(question_str)
    i = 0
    for c in tmp:
        if c in '!"$%&\'()*,-./:;<=>?@[\\]^_`{|}~“”':
            tmp[i] = " "
        i = i + 1
    question_file_handle.write(''.join(tmp))
    question_file_handle.write("\n")

"""
all_link_line = texts[1::4]  # 链接行列表
all_label_line = texts[2::4]  # 输出标签行列表
all_num_line = texts[3::4]  # 输出赞数行列表

for question in all_question_line:
    question_new = ''.join(c for c in question if c not in string.punctuation + '’‘“”')
    file_handle.write(question_new)
    file_handle.write('\n')
"""
