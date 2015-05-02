#!/usr/bin/env python
#coding:UTF-8

import re

pattern = re.compile('^hel')
m = pattern.match('hello world!')

if m:
    print m.group()
    print type(m.group())
else:
    print 'none'


