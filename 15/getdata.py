#!/usr/bin/env python
#coding:UTF-8

from random import randint, choice
from string import lowercase
from sys import maxint
from time import ctime
from sys import argv

f = open(argv[1], 'w+')

doms = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randint(5,10)):
    dtint = randint(0, 2^32-1)
    dtstr = ctime(dtint)
    #dtstr = ctime()

    shorter = randint(4, 7)
    em = ''
    for j in range(shorter):
        em += choice(lowercase)

    longer = randint(shorter, 12)
    dn = ''
    for j in range(longer):
        dn += choice(lowercase)

    f.write('%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, 
            dn, choice(doms), dtint, shorter, longer))
    f.write('\n')

    #return '%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, 
    #        dn, choice(doms), dtint, shorter, longer)
