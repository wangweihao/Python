#!/usr/bin/env python
#coding:UTF-8

import urllib
import re

def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getdata(obj):
    patt = r'(<dl>.+?>(9\.\d).+?</dl>)'
    #patt = r'<dl>.+</dl>'
    pattern = re.compile(patt, re.DOTALL)
    m = pattern.findall(obj)
    Len = len(m)
    print 'len: %d' % Len
    if m is not None:
        for i in m:
            print i[1],
        print
    else:
        print 'not found'
    if Len == 0:
        return False
    else:
        return True

def getnextpage(obj):
    nextpage = 'http://www.douban.com/tag/%E7%BC%96%E7%A8%8B/book?start='
    #patt = '(\d).+&gt'
    patt = '<span class="break">...</span>.+start=(\d+)'
    pattern = re.compile(patt, re.DOTALL)
    m = pattern.search(obj)
    if m is not None:
        #print m.group()
        nextpage += m.group(1)
    else:
        print 'not found'
    return nextpage



if __name__ == '__main__':
    #gain html data
    html = gethtml("http://www.douban.com/tag/%E7%BC%96%E7%A8%8B/book")
    #write into file
    f = open('douban', 'w+')
    f.write(html)
    
    
    while 1:
        if getdata(html) == False:
            break
        ret = getnextpage(html)
        html = gethtml(ret)


