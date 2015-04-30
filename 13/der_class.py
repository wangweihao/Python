#!/usr/bin/env python
#coding:UTF-8

class MyClass(object):
    glb = 100                #global variable
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph

    def func(self):
        print 'hello, i am myclass function'

class DerClass(MyClass):
    der_glb = 200               #global variable
    def __init__(self, nm, ph, addr):
        super(DerClass, self).__init__(nm, ph)   #python2
        #super.__init__(nm, ph)                  #python3
        #MyClass.__init__(self, nm, ph)
        self.address = addr

    def func(self):
        #print self.__class__
        print 'hello, i am derclass function'

    def __del__(self):
        print(self.__class__.der_glb)
        del self.__class__.der_glb
        #del self.der_glb
        print 'del der_glb'

if __name__ == '__main__':
    m1 = MyClass('wwh', '123')
    m2 = DerClass('wwh', '456', 'xian')
    print 'name:%s, phone:%s' % (m1.name, m1.phone)
    m1.func()
    print(m1.glb)
    m1.glb = 1000
    print(m1.glb)
    print 'name:%s, phone:%s, address:%s' % (m2.name, m2.phone, m2.address)
    m2.func()
    print(m2.der_glb)
    print(m2.glb)
    m3 = DerClass('ww', 'asd', 'aaa')
    print(m3.der_glb)
    

