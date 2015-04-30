#!/usr/bin/env python
#coding:UTF-8

import sys

class MyClass(object):
    def __init__(self):
        print('i am __init__ function')

    def __del__(self):
        print('i am __del__ function')


if __name__ == '__main__':
    m1 = MyClass()
    m2 = m1
    print(sys.getrefcount(m1))
