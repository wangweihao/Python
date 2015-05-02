#!/usr/bin/env python
#coding:UTF-8

import re

Str = 'hello world'
m = re.search('o w', Str)
if m is not None:
    print m.group()
    print type(m.group())
else:
    print 'not found'
