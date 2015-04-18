#!/usr/bin/env python
#coding:UtF-8

def trans(i,j):
    if(i % j == 0):
        return True
    else:
        return False

if __name__ == '__main__' :
    str = raw_input('please input two number:')
    st = str.split()
    print trans(int(st[0]), int(st[1]))
