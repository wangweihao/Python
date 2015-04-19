#!/usr/bin/env python
#coding:UTF-8

def ret(li, line):
    row = len(li)/line
    k = 0
    for i in range(row):
        for j in range(line):
            print li[k],
            k += 1
        print

if __name__ == '__main__':
    li = [1,2,3,4,5,6,7,8,9,10]
    ret(li,3)
