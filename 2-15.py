#!/usr/bin/env python
#coding:UTF-8

myTuple = []
for i in range(3):
    temp = raw_input('input:')
    myTuple.append(int(temp))
for i in range(3):
    print myTuple[i]
if myTuple[0] > myTuple[1]:
    temp = myTuple[0]
    myTuple[0] = myTuple[1]
    myTuple[1] = temp
if myTuple[0] > myTuple[2]:
    temp = myTuple[0]
    myTuple[0] = myTuple[2]
    myTuple[2] = temp
if myTuple[1] > myTuple[2]:
    temp = myTuple[1]
    myTuple[1] = myTuple[2]
    myTuple[2] = temp
for i in range(3):
    print myTuple[i],
