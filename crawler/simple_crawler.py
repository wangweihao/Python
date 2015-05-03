#!/usr/bin/env python
#coding:UTF-8

import urllib
import re

def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getdata(obj, patt):
    pattern = re.compile(patt)
    m = pattern.findall(obj)
    x = 0
    if m is not None:
        for i in m:
            print i 
            urllib.urlretrieve(i, './data/%s.jpg' % x)
            x += 1
    else:
        print 'not found'




if __name__ == '__main__':
    #gain html data
    html = gethtml("http://www.douban.com/tag/%E7%BC%96%E7%A8%8B/book")
    #write into file
    f = open('douban', 'w+')
    f.write(html)

    patt = r'http://\w{4}.douban.com/\w+/\w+.jpg'
    getdata(html, patt)


