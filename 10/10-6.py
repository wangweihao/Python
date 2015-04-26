#!/usr/bin/env python
#coding:UTF-8

def my_open(filename, mode):
    try:
        f = open(filename, mode)
    except:
        return None

if __name__ == '__main__':

