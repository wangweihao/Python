#!/usr/bin/env python
#coding:UTF-8

def dollarize(obj):
    ret = "'$"
    List = str(obj).split('.')
    #处理List[0],'.'前面的串
    ls = list(List[0])
    Len = len(ls)
    rge = Len/3
    for i in range(1, rge+1):
        ls.insert(Len-i*3, ',')
    #处理List[1],'.'后面的串
    ls2 = List[1][:2] + '.'
    return reduce(lambda ret,x:ret+x, ls, ret) + '.' + ls2

if __name__ == '__main__':
    print dollarize(1234567.8901)
    print dollarize(1000000.0000)

