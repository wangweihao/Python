#!/usr/bin/evn python
#coding:UTF-8


while 1:
    str = raw_input('请输入一个年份:')
    year = int(str)
    if ((year%4 == 0) and (year %100 == 0)) or ((year %4 == 0) and (year %100 != 0)):
        print 'year:%d is 润年' % year
    else:
        print 'year:%d is not 润年' % year
