#!/usr/bin/env python
#coding:UTF-8

import time

def mult(x,y):
    return x*y

def mul(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * mul(n-1)

seq = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

t1 = time.time()
print reduce(mult, seq)
t2 = time.time()
print (t2-t1) * 100

t3 = time.time()
print reduce(lambda x,y:x*y, seq)
t4 = time.time()
print (t4-t3) * 100

t5 = time.time()
print mul(16)
t6 = time.time()
print (t6-t5) * 100

