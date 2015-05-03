#!/usr/bin/env python
#coding:UTF-8

import re

patt = r'\w+(.+)\s'
s = 'aaabbb777提问者采纳    aaa'

pattern = re.compile(patt)
m = pattern.search(s)
if m is not None:
    print m.group(1)
else:
    print 'not found'
