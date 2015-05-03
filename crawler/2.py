#!/usr/bin/env python
#coding:UTF-8

def func(a):
    if a == 0:
        return False
    else:
        return True

i = 10
while 1:
    if func(i) == False:
        break
    else:
        print 'haha'
    i -= 1
