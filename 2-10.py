#!/usr/bin/env python
while 1 :
    x = raw_input('please input x 1-100:')
    if 1 < int(x) < 100:
        print 'success. '
        break
    else:
        print 'error.'
