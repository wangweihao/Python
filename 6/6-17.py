#!/usr/bin/env UTF-8
#coding:UTF-8

def myPop(li):
    del li[0]
    print li

if __name__ == '__main__':
    list = [1,2,3,4]
    myPop(list)
