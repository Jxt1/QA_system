# 字符串处理
import sys,os


def ques_str_op(ques_str):

    unexpected_form = ["What's","what's","where's","Where's","why's","Why's","When's","when's","How's","how's"]

    correctted_form = ["What is","what is","where is","Where is","why is","Why is","When is","when is","How is" "how is"]

    ques_op = ques_str

    for str in unexpected_form:
        result = str in ques_str
        if result:
            num = unexpected_form.index(str)
            str_new = correctted_form[num]

            pos_str = ques_op.find(str)
            ques_op = add_substr(ques_op, pos_str,str_new)
            ques_op = delete_substr(ques_op,str)
    s = "https://"
    if "/" in ques_op:
        if s in ques_op:
            return ques_op

        else:
            while "/" in ques_op:
                m = ques_op.index('/')
                ques_op = delete_substr(ques_op, '/')
                ques_op = add_substr(ques_op,m," ")
    return ques_op

def add_substr(str,pos_str,sub_str):
    ques_op_list = list(str)
    ques_op_list.insert(pos_str, sub_str)
    ques_op = "".join(ques_op_list)
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

print(ques_str_op("In SQL, what's the difference/between count(column) and count(*)?"))
