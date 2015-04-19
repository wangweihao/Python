#!/usr/bin/env python
#coding:UTF-8

dic = {1:'a', 2:'b', 3:'c'}
newdic = {}

for k in dic:
    newdic[dic[k]] = k

print newdic
