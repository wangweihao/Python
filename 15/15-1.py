#!/usr/bin/env python
#coding:UTF-8

import re

patt = 'b.t.* | hit'
m = re.search(patt, 'bitttttbat hit')
print m.group()

