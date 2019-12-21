import linecache
import distance

file_path = r'C:\dhj-learning\研一课程\自然语言处理\NLP-project\stackoverflow_index.txt'

count = -1
for count, line in enumerate(open(file_path, 'rb')):
    pass
count += 1

my_question = list(input("Enter your question: ").split())


def edit_distance(s1, s2):
    return distance.levenshtein(s1, s2)


number = []
context = []
for line_number in range(count):
    if line_number % 4 == 0:
        get_line = list(linecache.getline(file_path, line_number + 1).split())
        # print(get_line)
        now_line = ' '.join(get_line[1:])
        # print(now_line)
        # print(my_question)
        temp_i = edit_distance(my_question, now_line)
        number.append(temp_i)
        context.append([temp_i, line_number + 1, now_line])

temp_ii = number.index(min(number))
print(temp_ii)
print(context[temp_ii])

sort_number = sorted(range(len(number)), key=lambda i: number[i])
print(sort_number[1])
print(context[sort_number[1]])
print(sort_number[2])
print(context[sort_number[2]])
print(sort_number[3])
print(context[sort_number[3]])
