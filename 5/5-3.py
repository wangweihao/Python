#!/usr/bin/env python
#coding:UTF-8

while 1:
    x = raw_input('please a grade')
    gd = int(x)
    if 90 < gd < 100 :
        print 'A:'
    elif 80 < gd < 90 :
        print 'B:' 
    elif 70 < gd < 80 :
        print 'C:'
    elif 60 < gd < 70 :
        print 'D:'
    else:
        print 'F:'
