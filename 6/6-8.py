#!/usr/bin/env python
#coding:UTF-8


dict = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', \
        '7':'seven', '8':'eight', '9':'night'}
str = raw_input('please input a number (0-1000):')
list = []
for i in range(len(str)):
    list.append(str[i])

for j in range(len(list)):
    print dict[list[j]],
    if j == len(list)-1:
        break
    print '-',


