#!/usr/bin/env python
#coding:UTF-8

file_name1 = raw_input('please input filename1:')
file_name2 = raw_input('please input filename2:')

fd1 = open(file_name1, 'r+')
fd2 = open(file_name2, 'w+')

file_list = fd1.readlines()
fd2.writelines(file_list)


