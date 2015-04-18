#!/usr/bin/env python
#coding:UTF-8

import random

#produce a random number range 1,100
big_n = random.randint(1,101)
list = range(big_n)
for i in range(big_n):
    list[i] = random.randint(-1, 2**31)
list.sort()
print list
