#!/usr/bin/env python
#coding:UTF-8

def subchr(string, oldchar, newchar):
    str = ''
    for i in range(len(string)):
        if string[i] == oldchar:
            str += newchar
        else:
            str += string[i]

    return str

if __name__ == '__main__':
    s = 'abcdefff'
    oc = 'f'
    nc = 'e'
    print subchr(s, oc, nc)

