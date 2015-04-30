#!/usr/bin/env python
#coding:UTF-8

class Time60(object):
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min
    
    def __str__(self):
        return '%d:%d' % (self.hr, self.min)
    __repr__ = __str__

    def __add__(self, other):
        return self.__class__(self.hr + other.hr, 
                self.min + other.min)
        #return Time60(self.hr + other.hr, 
        #       self.min + other.min)
    
    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        return self

if __name__ == '__main__':
    t1 = Time60(10, 30)
    t2 = Time60(11, 15)
    print t1,t2
    print t1+t2
    print t1,t2
    t1 += t2
    print t1

