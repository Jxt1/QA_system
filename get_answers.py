#!/usr/bin/env python
# coding: utf-8

import requests 
from bs4 import BeautifulSoup
import pickle
import sys
import lxml
import re

##  通过链接从stackoverflow获取最佳答案
#   返回： vote数(int), 最佳答案(list), 评价(string)
#       最佳答案格式 = [文本(string), 代码(string), ...]
#       代码中在字符串头加$code$标记
def get_best_answer_on_url(url):
    try:
        html = requests.get(url)
    except Exception as e:
        print(e)
    soup = BeautifulSoup(html.text,'lxml')
    if soup.body.find(id = 'answers'):
        accepted = soup.find('div', {'class' : 'answer accepted-answer'})
        ans = accepted and accepted or soup.find('div', {'class' : 'answer'})
        
        votes = ans.find('div', {'class' : 'js-vote-count grid--cell fc-black-500 fs-title grid fd-column ai-center'})
        text = ans.find('div', {'class' : 'post-text'})
        comments = ans.find_all('span', {'class' : 'comment-copy'})
        
        text = str(text)
        text = re.sub(r'<code>', '@code@$code$\n', text)
        text = re.sub(r'</code>', '@code@', text)
        text = re.sub(r'<.*?>', '', text)
        text = text.replace('&gt;', '>')
        text = text.replace('&lt;', '<')
        text = text.split('@code@')
        
        if text[-1] == '\n':
            text.pop()
        if text[0] == '\n':
            text.pop(0)

        comments = str(comments)
        comments = re.sub(r'<.*?>', '', comments)
        comments = comments.replace('&gt;', '>')
        comments = comments.replace('&lt;', '<')
        
        return votes['data-value'], text, comments[1: -1]

if __name__ == "__main__":
    url = "https://stackoverflow.com/questions/40785224/tensorflow-cannot-interpret-feed-dict-key-as-tensor"
    url2 = 'https://stackoverflow.com/questions/11633021/automapper-expression-must-resolve-to-top-level-member'

    vote, ans, comment = get_best_answer_on_url(url)
    
    print(ans)
    print(ans[0])
    print(ans[1])





