#/usr/bin/env python
#coding:UTF-8

from primecal import*

def Perfect_num(x):
    List = PrimeCal(x)
    List.append(1)
    if sum(List) == x:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print Perfect_num(6)
    print Perfect_num(7)
