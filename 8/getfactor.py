#!/usr/bin/env python
#coding:UTF-8

def getfactors(x):
    ret = []
    count = x/2-1
    for i in range(1,count+1):
        if(x % i == 0):
            if x/i != i:
                ret.append(i)
            ret.append(x/i)
    return ret

if __name__ == '__main__':
    print getfactors(4)
    print getfactors(10)
