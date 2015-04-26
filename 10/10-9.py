#!/usr/bin/env python
#coding:UTF-8
import math, cmath

def my_mathsqrt():
    val = input()
    try:
        ret = math.sqrt(val)
    except:
        ret = cmath.sqrt(val)
    return ret

if __name__ == '__main__':
    my_mathsqrt()
