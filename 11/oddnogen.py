#!/usr/bin/env python
#coding:UTF-8

from random import randint 
 
#allNums = []
#for eachNum in range(9):
#    allNums.append(randint(1,99))
#print filter((lambda n:n%2), allNums)
#print [n for n in allNums if n%2]

print [n for n in [randint(1,99) for i in range(9)] if n %2]
