## Day 16: Exceptions - String to Integer
## https://www.hackerrank.com/challenges/30-exceptions-string-to-integer

import sys

S = raw_input().strip()

try:
    print int(S)
except ValueError:
    print 'Bad String'
    
    