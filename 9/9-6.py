#!/usr/bin/env python
#coding:UTF-8

fd1 = open('1.txt', 'r')
fd2 = open('2.txt', 'r')

for i in range(10):
    str1 = fd1.readline()
    str2 = fd2.readline()
    if str1 == str2:
        continue
    else:
        print i
        len = len(str1)
        if len(str2) < len:
            len = len(str2)
        for j in range(len):
            if str1[j] != str2[j]:
                print j
                break
