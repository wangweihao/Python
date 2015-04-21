#/usr/bin/env python
#coding:UTF-8

def Fibonacci(n):
    s = 1
    t = 1
    for i in range(n-2):
        temp = s
        s += t
        t = temp
    return s

if __name__ == '__main__':
    print Fibonacci(6)
