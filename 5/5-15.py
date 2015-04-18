#!/usr/bin/env python
#coding:UTF-8

str = raw_input('please input two number:')
num = str.split()
i = int(num[0])
j = int(num[1])

s = 1
while 1:
    if s % i == 0 and s % j == 0:
        print s
        break
    else:
        s+=1

max = i
if(j > i):
    max = j
ret = 1

print i,j

for t in range(1,max):
    if i % t == 0 and j % t == 0:
        ret = t
print ret
