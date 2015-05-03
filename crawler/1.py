#!/usr/bin/env python
#coding:UTF-8

import re

s1 = 'aaaa1234'
s2 = 'aaaa123'
s3 = 'aaaa12'
s4 = 'aaaa1'
patt = 'aaaa(\d+)'
m = re.search(patt, s1)
print m.group()
print m.group(1)
