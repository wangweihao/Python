#!/usr/bin/env python
#coding:UTF-8

def fiboni(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fiboni(n-1) + fiboni(n-2)

if __name__ == '__main__':
    for i in range(20):
        print fiboni(i)

