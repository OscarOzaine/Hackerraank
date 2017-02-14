#Extra Long Factorials
#https://www.hackerrank.com/challenges/extra-long-factorials

import sys

n = int(raw_input().strip())

factorial = 0
for x in range(n, 2, -1):
    n = n * (x - 1)
    
print n
    