#!/usr/bin/env python
#coding:UTF-8

while 1:
    str = raw_input('输入一个小于100美分的数字:')
    num = int(str)
    i = num / 25
    print '25美分 is %d' % i
    j = (num - i*25) / 10
    print '10美分 is %d' % j
    k = (num - i*25 - j*10) / 1
    print '1美分 is %d' % k
