#!/usr/bin/env python3

from random import choice

"""
Deutsch oracle / alogrithm experimentation.


Futher reading:
https://www.quiprocone.org/Protected/DD_lectures.htm

"""


class Oracle:
    # Black-box oracle that implements an initially unknown one-bit Boolean function.
    # One bit functions:
    #      Constant:                 Balanced:
    #      f0           f1           fx           fx̄
    FNS = [lambda x: 0, lambda x: 1, lambda x: x, lambda x: 1 - x]

    def __init__(self):
        self.function = choice(self.FNS)

    def f(self, b):
        return self.function(b)


class OracleRev(Oracle):
    # Reversible, (non-quantum), 2 bit in 2 bit out version, using y input value for constant fns.
    # Assumes y = 0 by default, (although it doesn't have to be).
    FNS = [
            lambda x, y: (x, y),
            lambda x, y: (x, 1 - y),
            lambda x, y: (x, x),
            lambda x, y: (x, 1 - x)
    ]

    def f(self, b, r=0):
        return self.function(b, r)


class Oracle2F(OracleRev):
    # Not-quite-(!)-Reversible, (non-quantum), 2 bit in 2 bit out version:
    FNS = [
            lambda x, y: (x, 0),  # hardcoded 0 loses info about y
            lambda x, y: (x, 1),  # hardcoded 1 loses info about y
            lambda x, y: (x, x),
            lambda x, y: (x, 1 - x)
    ]


if __name__ == '__main__':
    o = OracleRev()
    print(o)
    print('0:', o.f(0))
    print('1:', o.f(1))
