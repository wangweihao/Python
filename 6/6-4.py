#!/usr/bin/env python
#coding:UTF-8

grade = []
while 1:
    gd = input('please a grade')
    if gd == -1:
        break
    grade.append(gd)
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

#avg = sum(grade)/len(grade)
#print 'average is %d' % avg

print 'average is %lf' % (float(sum(grade))/len(grade))

