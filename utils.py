

# 字符串处理
import sys,os


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

def ques_str_op(ques_str):

    unexpected_form = ["What's","what's","where's","Where's","why's","Why's","When's","when's"]

    correctted_form = ["What is","what is","where is","Where is","why is","Why is","When is","when is"]

    ques_op = ques_str

    for str in unexpected_form:
        result = str in ques_str
        if result:
            num = unexpected_form.index(str)
            str_new = correctted_form[num]
            pos_str = ques_op.find(str)

            ques_op_list = list(ques_op)
            ques_op_list.insert(pos_str,str_new)
            ques_op = "".join(ques_op_list)
            ques_op = delete_substr(ques_op,str)

    if "/" in ques_op:
        n = ques_op.index("/")
        if (ques_op[n-1] > 'A' or ques_op[n-1])<'z' or (ques_op[n+1] > 'A' or ques_op[n+1]<'z' ):
            ques_op = delete_substr(ques_op, '/')

    return ques_op


def delete_substr(in_str, in_substr):
  start_loc = in_str.find(in_substr)
  in_str, in_substr = list(in_str), list(in_substr)
  [len_str, len_substr] = len(in_str), len(in_substr)
  res_str = in_str[:start_loc]
  for i in range(start_loc + len_substr, len_str):
    res_str.append(in_str[i])
  res = ''.join(res_str)
  return res

if __name__ == "__main__":
    # pass
    print(ques_str_op("In SQL, what's the difference between count(column) and count(*)?"))

