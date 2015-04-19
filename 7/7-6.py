#!/usr/bin/env python
#coding:UTF-8

db = []

while True:
    prompt = """
    occur   num   price   c_price

    Enter:"""
    item = raw_input(prompt)
    if item == 'q':
        break
    list = item.split()
    if len(list) != 4:
        print 'error!'
        break
    db.append(list)
 

mp = {}
while True:
    prompt = """
    (1)occur
    (2)num
    (3)price
    (4)c_price

    Enter:"""
    index = input(prompt)-1
    for li in db:
        t = li[index]
        del li[index]
        mp[t] = li
    tmp = sorted(mp.iteritems(), key = lambda li:li[0])
    print tmp

