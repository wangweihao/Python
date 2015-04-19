#!usr/bin/env python
#coding:UTF-8

from string import Template
s= Template('there are ${howmany} ${haha} aa')
print s.substitute(howmany = 'aaa', haha = 1)
#print s.substitute(howmany = 'aaa')
print s.safe_substitute(howmany = 'aaa')
