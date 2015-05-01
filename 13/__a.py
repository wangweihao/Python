#!/usr/bin/env python
#coding:UTF-8

class MyClass(object):
    __foo = 200
    _bar = 1000
    def func(self):
        print self.__foo
        print self._bar

if __name__ == '__main__':
    m = MyClass()
    m.func()
    m.__foo = 2000
    m._bar = 100
    m.func()
    print m.__foo
    print m._MyClass__foo

