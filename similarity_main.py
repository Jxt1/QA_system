"""
TODO
1、question处理（标点与特殊符号的处理） ==> process_question.py ok
2、统计所有（去掉重用词外）词及其词频（用dictory处理） ==> count_word.py  ok
3、给每个词定义一个id（与词频有关） ==> word2id.py   ok
4、每个句子成为一个list  ==>
5、所有句子append成一个大list（类似二维向量从左到右递增，从上到下递增）其对应的
问题序号也append成一个对应的list
[[……],
……
[……]]
//
6、对用户输入的问题，转换成list（这一步也要求有个dictory文件）
7、查找（相似的词数超过输入句子的一多半 2/3 时输出，可能会输出多条）


a b c
0 1 2

a b: 0 1
b c :2 3

d = dict()
cnt = 0
for word in words:
	d[word] = cnt 
	cnt = cnt + 1

print d["char"]
"""
