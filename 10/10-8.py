#!/usr/bin/env python
#coding:UTF-8

def safe_input():
    try:
        retval = raw_input()
    except (KeyboardInterrupt, EOFError):
        retval = None

    return retval

if __name__ == '__main__':
    safe_input()
