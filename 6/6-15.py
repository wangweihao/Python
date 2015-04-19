#!/usr/bin/env python
#coding:UTF-8

def cal(data):
    li = data.split('/')
    i = int(li[0])
    j = int(li[1])
    k = int(li[2])
    #sum = int(li[0])*365 + int(li[1])*30 + int(li[2])*1
    sum = i*365 + j *30 + k*1
    return sum

def calcu(data1, data2):
    ret = cal(data1) - cal(data2)
    return abs(ret)

if __name__ == '__main__':
    while 1:
        str1 = raw_input('data_one:')
        str2 = raw_input('data_two:')
        print 'result:%d' % calcu(str1, str2)
