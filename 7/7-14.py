#!/usr/bin/env python 
#coding:UTF-8

import random

#while True:
num1 = random.randint(1,10)
num2 = random.randint(1,10)
s1 = set()
s2 = set()
for i in range(num1):
    s1.add(random.randrange(0,10))
for i in range(num2):
    s2.add(random.randrange(0,10))

print 's1:',s1
print 's2:',s2
print s1 & s2
print s1 | s2

        

