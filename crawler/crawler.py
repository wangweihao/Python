#!/usr/bin/env python
#coding:UTF-8

import urllib
import re

def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


html = gethtml("http://book.douban.com/")
f = open('douban', 'w+')
f.write(html)


patt = r'http://\w{4}.douban.com/\w+/\w+.jpg'
pattern = re.compile(patt)
m = pattern.findall(html)

x = 0
if m is not None:
    for i in m:
        print i
        urllib.urlretrieve(i, './data/%s.jpg' % x)
        x += 1
else:
    print 'not found'


