#!/usr/bin/env python
#coding:UTF-8

try:
    fd = open('a', 'rb')
except IOError,e:
    print 'could not open file:', e

print 'haha'
