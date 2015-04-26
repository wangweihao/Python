#!/usr/bin/env python
#coding:UTF-8

name = raw_input('please file name:')
fd = open(name, 'r')
i = 0
for line in fd:
    i += 1
    if i%26 == 0:
        print 
    print i,line,
