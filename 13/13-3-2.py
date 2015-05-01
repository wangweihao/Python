#!/usr/bin/env python
#coding:UTF-8


class MoneyFmt(object):
    def __init__(self, obj):
        self.s = obj

    def __str__(self):
        return str(self.s)
    __repr__ = __str__
    
    def __nonzero__(self):
        return self.s == '0'

    def dollarize(self):
        ret = "'$"
        List = str(self.s).split('.')
        #处理List[0],'.'前面的串
        ls = list(List[0])
        Len = len(ls)
        rge = Len/3
        for i in range(1, rge+1):
            ls.insert(Len-i*3, ',')
        #处理List[1],'.'后面的串
        ls2 = List[1][:2] + '.'
        self.s = reduce(lambda ret,x:ret+x, ls, ret) + '.' + ls2
        return self.s

    def update(self, newobj):
        self.s = newobj



if __name__ == '__main__':
    s = MoneyFmt('1234567.8901')
    print s
    print s.dollarize()
    s.update('123456789.8888')
    print s.dollarize()
    print s.__str__()
