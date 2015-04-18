#!/usr/bin/env python
#coding:UTF-8


while 1:
    ele = raw_input()
    ret = ele.split();
    if ret[1] == '*':
        result = int(ret[0]) * int(ret[2])
        print 'result:%d' % result
    elif ret[1] == '+':
        result = int(ret[0]) + int(ret[2])
        print 'result:%d' % result
    elif ret[1] == '-':
        result = int(ret[0]) - int(ret[2])
        print 'result:%d' % result
    elif ret[1] == '/':
        result = int(ret[0]) / int(ret[2])
        print 'result:%d' % result


