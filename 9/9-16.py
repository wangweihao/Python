#!/usr/bin/env python
#coding:UTF-8

file_name = raw_input('please input a filaname:')
fd = open(file_name, 'r+')
Str = fd.read()
List = Str.split()
space = ' '
eachline = ''
Len = 0
l = 0

for eachword in List:
    if Len >= 80:
        eachline2 = eachline[:Len-l]
        lastLen = 80 - len(eachline2)
        if lastLen > (l-1)/2:
            print eachline
            eachline = ''
            Len = 0
        else:
            print eachline2
            eachline = last_word + space
            Len = l
    last_word = eachword
    eachline += eachword
    eachline += space
    l = len(eachword) + 1     # 1 is space size
    Len += l                   
 
