#!/usr/bin/env python
#coding:UTF-8

flag = False
str = raw_input('please input a time:')
for i in range(len(str)):
    if str[i] == ':':
        flag = True

if(flag == True):
    time = str.split(':')
    print int(time[0])*60 + int(time[1])
else:
    print int(str)
