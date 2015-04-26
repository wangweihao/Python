#!/usr/bin/env python
#coding:UTF-8

import getopt, sys
# "-x 'argument'"  "-v 'argument'" "-f"
shortargs = 'x:v:f'
# "--help"  "--ip='argument'"  "--port='argument'"
longargs = ['--help', 'ip=', 'port=']
print getopt.getopt(sys.argv[1:], shortargs, longargs)


