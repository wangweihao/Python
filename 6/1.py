#!/usr/bin/env python
#coding:UTF-8

str = 'abcdefghijklmn'
for i in str:
    print i

for i in range(len(str)):
    print str[i]

for i in enumerate(str):
    print i

num = [1,2,3,4,5,6]
print max(num, None)

iter = reversed(num)
print iter
