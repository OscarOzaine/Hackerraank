#!/bin/python

import sys

n = int(raw_input().strip())

binary = []
while(n > 0):
    remainder = n % 2;
    n = n/2;
    binary.append(remainder)
    
count = 0
max_count = 0
for i in reversed(binary):
    if i == 1:
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 0
print max_count

