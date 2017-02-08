#!/bin/python
#arrays-ds
#Hackerrank.com
import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for a in reversed(arr):
    print a,
    