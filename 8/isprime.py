#!/usr/bin/env python
#coding:UTF-8

def isprime(x):
    count = x/2
    flag = 0
    while count != 1:
        if x%count == 0:
            flag = 1
            break
        count -= 1
    if flag == 1:
        return False
    else:
        return True

if __name__ == '__main__':
    print isprime(37)
