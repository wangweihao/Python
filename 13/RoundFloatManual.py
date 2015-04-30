#!/usr/bin/env python
#coding:UTF-8

class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), \
                "Value must be a float!"
        self.value = round(val, 2)

    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
    rfm = RoundFloatManual(4.2)
    print rfm
