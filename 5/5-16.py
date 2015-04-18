#!/usr/bin/env python
#coding:UTF-8

str1 = raw_input('Enter opening balance:')
str2 = raw_input('monthly payment:')
Sum = float(str1)
pay = float(str2)
print 'Pymt#    Paid      balance'
i = 0
print '%4d     $0        $%.2f' % (i, Sum)
while Sum > pay:
    i += 1
    Sum -= pay
    print '%d        $%.2f   $%.2f' % (i, pay, Sum)
print '%d       $%.2f     $0' % (i, Sum)
    
