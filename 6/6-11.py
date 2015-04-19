#!/usr/bin/env python
#coding:UTF-8

num = input('please input a number')
str = str(num)
s = ''
for i in range(0, len(str)):
    if i%3 == 0:
        s += '.'
    s += str[i]
ret = s[1:]

print ret
