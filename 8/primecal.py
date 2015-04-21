#!/usr/bin/env python
#coding:UTF-8

#import isprime
#import getfactor

from isprime import*
from getfactor import*

def PrimeCal(x):
    ret = []
    i = 2
    while x != 1:
        if x % i == 0:
            x /= i
            ret.append(i)
        else:
            while 1:
                i += 1
                if isprime(i) == True:
                    break

    return ret


if __name__ == '__main__':
    print PrimeCal(20)
