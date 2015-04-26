#!/usr/bin/env python
#coding:UTF-8

import sys
N = sys.argv[1]
F = sys.argv[2]

fds = open(F, 'r')
for i in range(int(N)):
    str = fds.readline()
    print str,
