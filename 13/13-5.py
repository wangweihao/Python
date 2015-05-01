#!/usr/bin/env python
#coding:UTF-8

class Point(object):
    def __init__(self, X = 0, Y = 0):
        self.x = X
        self.y = Y

    def Print(self):
        print 'x:%d, y:%d' % (self.x, self.y)

if __name__ == '__main__':
    p = Point(1)
    p.Print()
