#!usr/bin/env python
#coding:UTF-8

def trans(f):
    d = (f - 32) * (5.0/9)
    return d

while 1:
    str = raw_input('input the f:')
    print trans(int(str))
