#/usr/bin/env python
#coding:UTF-8

def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum

if __name__ == '__main__':
    print factorial(4)
