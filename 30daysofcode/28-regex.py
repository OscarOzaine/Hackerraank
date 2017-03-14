## Day 28: RegEx, Patterns, and Intro to Databases
## https://www.hackerrank.com/challenges/30-regex-patterns

import sys
import re

N = int(raw_input().strip())
q = []
for a0 in xrange(N):
    firstName,emailID = raw_input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    
    e = re.search('@gmail.com', emailID)
    if e != None:
        q.append(firstName)

q = sorted(q)
for i in q:
    print i