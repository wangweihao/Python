#!/usr/bin/env python
#coding:UTF-8

while 1:                 
    myTuple = []
    i = 0
    sum = 0
    print '1.取5个数的和\n2.取5个数的平均数\nx.退出\n'
    x = raw_input('please choose function:')
    if x == '1':
        for i in range(5):
            temp = raw_input('input:')
            myTuple.append(int(temp))
        for j in range(5):
            sum += myTuple[i]
        print 'sum %d' % sum
    elif x == '2':
        for i in range(5):
            temp = raw_input('input:')
            myTuple.append(int(temp))
            sum += myTuple[i]
        print 'sum:%d' % sum
        print 'avg:%lf' % (float(sum)/i)
    elif x == 'x':
        print 'quit'
        break
    print
