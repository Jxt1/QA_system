from get_answers import get_best_answer_on_url
from question_classifier import classify
from AnswerExtractor.AE1 import check_in

fout = open('./data/OB.txt', "w", encoding='utf-8')
cnt = 0
with open('./data/stackoverflow_index.txt', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        if i % 4 == 0:
            line = lines[i]
            a = line.find(' ')
            question = line[a+1:]

            try:
                Q_type = classify(question) 
            except Exception as e:
                Q_type = 6

            link = lines[i+1].strip('\n')
            response = get_best_answer_on_url(link)
            answer_raw = response[1][1]
            # break
            if Q_type==1:
                # print(Q_type, question, answer_raw)
                
                # print(question)
                # for e in answer_raw:
                #     print(e)
                # print('')

                fout.write(question)
                for e in answer_raw:
                    if check_in(question, e):
                        fout.write(e)
                fout.write('***************************************************')
                # cnt = cnt + 1
                
                # break
print(cnt)
fout.close()
