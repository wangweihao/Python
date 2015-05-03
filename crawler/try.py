#!/usr/bin/env python
#coding:UTF-8

import re

s = 'aaa    bbb   333-333'
patt = '.*\d-\d'
pattern = re.compile(patt)
m = pattern.search(s)
print m.group()

