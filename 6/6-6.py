#!/usr/bin/env python
#coding:UTF-8

str = raw_input('please input a string:')
list = []
for i in range(0, len(str)):
    if str[i] != ' ':
        list.append(i)
        break

for i in range(i, len(str)):
    if str[i] == ' ':
        list.append(i)
        break
if list[0] == 0:
    print str
else:
    ret = str[list[0]:list[1]]
    print ret

