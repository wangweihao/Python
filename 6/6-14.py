#!/usr/bin/env python
#coding:UTF-8


dict = {1:'s', 2:'j', 3:'b'}
cal = {('s','j'):True, ('s','b'):False, ('s','s'):False,
        ('j','b'):True, ('j', 's'):False, ('j','j'):False,
        ('b','s'):True, ('b', 'j'):False, ('b','b'):False}

import random
def Rochambeau():
    ret = random.randint(1,3)
    return dict[ret]

def Rochcalcu(m, n):
    aTuple = (m,n)
    return cal[aTuple]



if __name__ == '__main__':
    while 1:
        """   1.'ST'
              2.'JD'
              3.'B'"""
        s = input('please input(1-3):')
        i = dict[s]
        j = Rochambeau()
        result = Rochcalcu(i, j)
        if result == True:
            print 'you %s  computer %s ' % (i,j)
            print 'you are win'
        else:
            print i,j
            print 'you are falut'

