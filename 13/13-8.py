#!/usr/bin/env python
#coding:UTF-8

class Stack(object):
    stack = []
    def __init__(self, obj):
        self.stack = obj

    def pop(self):
        if 'pop' in dir(self.stack):
            return self.stack.pop()
        else:
            index = len(self.stack)-1
            ret = self.stack(index)
            self.stack.remove(ret)
            return ret

    def push(self, ele):
        self.stack.append(ele)

    def isempty(self):
        return bool(len(self.stack))

    def peek(self):
        return self.stack[len(self.stack)-1]

    def Print(self):
        for i in self.stack:
            print i,
        print

if __name__ == '__main__':
    s = Stack([1,2,3])
    s.Print()
    s.push(1)
    s.Print()
    print 'peek:%d' % (s.peek())
    s.pop()
    s.Print()
    print 'peek:%d' % (s.peek())


