#!/usr/bin/env python
#coding:UTF-8

class NumStr(object):

    def __init__(self, num = 0, string = ''):
        self._num = num
        self._string = string

    def __str__(self):
        return '[%d::%r]' % \
                (self._num, self._string)
    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other, NumStr):
            return self.__class__(self._num + other._num,  
                    self._string + other._string)
        else:
            raise TypeError, \
                    'Illegal argument type for built-in operation'

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self._num * num, 
                    self._string * num)
        else:
            raise TypeError, \
                    'Illegal argument type for built-in operation'

    def __nonzero__(self):
        return self.__num or len(self._string)

    def _norm_cval(self, cmpres):
        return cmp(cmpres, 0)

    def __cmp__(self, other):
        return self.__norm_cval(
                cmp(self._num, other._num)) + \
                        self.__norm_cval(            
                                cmp(self._string, other._string))



if __name__ == '__main__':
    a = NumStr(3, 'foo')
    b = NumStr(3, 'goo')
    c = NumStr(2, 'foo')
    d = NumStr()
    e = NumStr(string = 'boo')
    f = NumStr(1)
    print a
    print b
    print a==a
    print b*2
    print a*3
    print b+e
