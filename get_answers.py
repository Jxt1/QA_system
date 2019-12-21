#!/usr/bin/env python
# coding: utf-8

import requests 
from bs4 import BeautifulSoup
import pickle
import sys
import lxml
import re

##  通过链接从stackoverflow获取最佳答案
#   返回值：
#           状态, (vote数, 答案, 评论)
#         状态: 
#               1.访问出错, "Access error"
#               2.没有答案, "No answer"
#               3.最佳答案, "Accept answer" 
#               4.vote数最高答案, "Votes answer"
#         vote数
#         答案(list), 格式 = [文本(string), 代码(string), ...], 代码中在字符串头加$code$标记
#         评论(list), 格式 = [评论1, 评论2, ...]
def get_best_answer_on_url(url):
    while True:
        html = ''
        try:
            html = requests.get(url, timeout=5)
        except Exception as e:
            print(e)
            # return "Access error"
        if html != '':
            break
    soup = BeautifulSoup(html.text,'lxml')
    if soup.body.find('div', {'class': 'no-answers'}):
        return "No answer"
    
    else:
        accepted = soup.find('div', {'class' : 'answer accepted-answer'})
        ans = accepted and accepted or soup.find('div', {'class' : 'answer'})

        votes = ans.find('div', {'class' : 'js-vote-count grid--cell fc-black-500 fs-title grid fd-column ai-center'})
        text = ans.find('div', {'class' : 'post-text'})
        comments = ans.find_all('span', {'class' : 'comment-copy'})

        text = str(text)
        text = re.sub(r'<code>', '@code@$code$', text)
        text = re.sub(r'</code>', '@code@', text)
        text = re.sub(r'<.*?>', '', text)
        text = text.replace('&gt;', '>')
        text = text.replace('&lt;', '<')
        text = text.split('@code@')

        if text[-1] == '\n':
            text.pop()
        if text[0] == '\n':
            text.pop(0)
            
        for i in range(len(comments)):
            comment = str(comments[i])
            comment = re.sub(r'<.*?>', '', comment)
            comment = comment.replace('&gt;', '>')
            comment = comment.replace('&lt;', '<')
            comments[i] = comment
            
        return accepted and "Accept answer" or "Votes answer", (votes['data-value'], text, comments)

if __name__ == "__main__":
    url_invalid = ""
    url_no_answer = "https://stackoverflow.com/questions/59351022/intellij-unable-to-use-bin-bash"
    url_accept_answer = "https://stackoverflow.com/questions/40785224/tensorflow-cannot-interpret-feed-dict-key-as-tensor"
    url_vote_answer = 'https://stackoverflow.com/questions/11633021/automapper-expression-must-resolve-to-top-level-member'

    response = get_best_answer_on_url(url_invalid)
    if response == "No answer" or response == "Access error":
        print(response)
    else:
        votes, ans, comments = response[1]
        print(ans)
        print(comments)

    response = get_best_answer_on_url(url_no_answer)
    if response == "No answer" or response == "Access error":
        print(response)
    else:
        votes, ans, comments = response[1]
        print(ans)
        print(comments)
        
    response = get_best_answer_on_url(url_accept_answer)
    if response == "No answer" or response == "Access error":
        print(response)
    else:
        print(response[0])
        votes, ans, comments = response[1]
        print(ans)
        print(comments)
        
    response = get_best_answer_on_url(url_vote_answer)
    if response == "No answer" or response == "Access error":
        print(response)
    else:
        print(response[0])
        votes, ans, comments = response[1]
        print(ans)
        print(comments)
