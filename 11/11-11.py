#!/usr/bin/env python
#coding:UTF-8

def clear_file(filename):
    f = open(filename, 'r+')
    newlines = map(lambda x:x.split(), f)
    s = raw_input('new filename:')
    f2 = open(s, 'w+')
    for line in newlines:
        f2.write(line[0]+'\n')

if __name__ == '__main__':
    clear_file('1')
