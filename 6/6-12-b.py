#!/usr/bin/env python
#coding:UTF-8

def rfindchr(string, char):
    index = 0
    for i in range(len(string)):
        if(string[i] == char):
            index = i
    return index

if __name__ == '__main__':
    str = 'ababab'
    c = 'a'
    print rfindchr(str, c)
