## Day 29: Bitwise AND
## https://www.hackerrank.com/challenges/30-bitwise-and

import sys

t = int(raw_input().strip())

for i in range(0, t):
    n_temp = raw_input().strip().split(' ')
    n = int(n_temp[0])
    k = int(n_temp[1])
    
    a = k - 1
    b = (~a) & -(~a)
    
    if (a | b) > n:
        print a - 1
    else:
        print a

        