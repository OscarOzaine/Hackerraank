#!/bin/python

import sys

t = int(raw_input().strip())

for a0 in xrange(t):
    n = int(raw_input().strip())
    
    growth = 0
    for x in range(0, n + 1):
        if (x % 2) != 0:
            growth = growth * 2
        else:
            growth = growth + 1
    print growth
    