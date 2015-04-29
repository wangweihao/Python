#!/usr/bin/env python
#coding:UTF-8

def pri_str(s, n):
    if n == 0:
        return 0
    
    print s[n-1]  #反向
    pri_str(s, n-1)
    #print s[n-1]  正向

if __name__ == '__main__':
    s = 'abcdef'
    pri_str(s, len(s))
