#!/usr/bin/env python
#coding:UTF-8
filename = raw_input('filename:')
fobj = open(filename, 'r')
for eachLine in fobj:
    print eachLine,
fobj.close()
