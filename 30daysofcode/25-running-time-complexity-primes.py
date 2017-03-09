## Day 25: Running Time and Complexity
## https://www.hackerrank.com/challenges/30-running-time-and-complexity

import math

def isPrime(number):
    if number < 2:
        return False
    
    if len(str(number)) > 5:
        sqnumber = int(math.sqrt(number))
    else:
        sqnumber = number
    
    for i in range(2, sqnumber):
        if number % i == 0:
            return False
        
    return True

N = int(raw_input().strip())

for n in range(0, N):
    
    n = int(raw_input().strip())
    if isPrime(n):
        print 'Prime'
    else:
        print 'Not prime'
