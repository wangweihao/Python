#!/usr/bin/env python
#coding:UTF-8

import re

s = 'helloworld800-333-3333'
patt = '.+?(\d+-\d+-\d+)'

m = re.search(patt, s)
print m.group(1)
