#!/usr/bin/env python
#coding:UTF-8

def findchr(string, char):
    print string, char
    for i in range(len(string)):
        if char == string[i]:
            break
    if i == len(string)-1:
        return -1
    else:
        return i

if __name__ == '__main__':
    str = 'abcdef'
    c = 'a'
    d = 'p'
    print findchr(str, c)
    print findchr(str, d)
