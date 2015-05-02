#!/usr/bin/env python
#coding:UTF-8

import sys
prev_exit_func = getattr(sys, 'exitfunc', None)

def my_exit_func(old_exit = prev_exit_func):
    print 'hahahahhaha'

if old_exit is not None and callable(old_exit):
    old_exit()

sys.exitfunc = my_exit_func

if __name__ == '__main__':
    print '11'
    os.exit()
