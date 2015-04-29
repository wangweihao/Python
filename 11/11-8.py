#!/usr/bin/env python
#coding:UTF-8

def func(n):
    return n%2==0

seq = [1,2,3,4,5,6,7,8,9]

print filter(func, seq)
