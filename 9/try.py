#!/usr/bin/env python
#coding:UTF-8

def safe_float(obj):
    try:
        float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    return retval

if __name__ == '__main__':
    print safe_float('p')
