# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
pip install ptt.py


from ptt import Board

Board_Name = "gossiping"

title = []\\latest_page = Board(Board_Name)

for summary in latest_page:
    print('正在抓取資料中...' + summary.title)
    if summary.isremoved:
        continue
    try:
        article = summary.read()
    except:
        pass
    
    titles.append(article.title)
    
print(titles)

question = []
for i in titles:
    if '問卦' in 1:
        question.append(i)
        
print(question)