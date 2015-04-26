#!/usr/bin/env python
#coding:UTF-8

import sys
filename = sys.argv[1]

fd = open(filename, 'r')
for eachline in fd:
    if '#' in eachline:
        if '#' != eachline[0]:
            linelist = eachline.split('#')
            eachline = linelist[0]
        else:
            continue
    Llist = eachline.split()
    for each_ele in Llist:
        print each_ele,
    print 
