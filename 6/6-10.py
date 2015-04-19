#!/usr/bin/env python
#coding:UTF-8

def trans(str): 
    s = ''
    for c in str:
        if c.isupper():
            s += c.lower()
        else:
            s += c.upper()
    return s

if __name__ == '__main__':
    s = raw_input('please input a string:')
    print trans(s)
