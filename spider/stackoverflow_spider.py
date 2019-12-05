import requests 
from bs4 import    BeautifulSoup
import pickle
import sys
sys.setrecursionlimit(10000)

data = []
f = open('./data/stackoverflow_index.txt','a+',encoding='utf-8')

cnt = 0

try:
    for page in range(1,372517):
        print(page, cnt)
        url = 'https://stackoverflow.com/questions?page={}&sort=votes&pagesize=50/'.format(page)
        strhtml = None
        while True:
            try:
                strhtml = requests.get(url)        #Get方式获取网页数据
                break
            except Exception as e:
                print(e)
        soup=BeautifulSoup(str(strhtml.content).encode('utf-8',),'lxml')
        for i, child in enumerate(soup.body.find(id='questions').children):
            if child.find('h3') == -1:
                continue
            link = 'https://stackoverflow.com' + child.h3.a['href']
            question = child.h3.a.string
            tags =  [x[2:] for x in child.h3.next_sibling.next_sibling.next_sibling.next_sibling['class'][1:]]
            answer_number = child.strong.string
            data.append({'link': link, 'question': question, 'tags': tags, 'answer_number':answer_number})

            cnt = cnt + 1
            f.write('{} {}\n'.format(cnt,question))
            f.write(link+'\n')
            f.write(str(tags)+'\n')
            f.write(answer_number+'\n')
except Exception as e:
    print(str(e))

# pickle.dump(data,open('./data/stackoverflow_index', 'wb') )

