'''
	Sample Input
	2
	12
	1012

	Sample Output

	2
	3
'''

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    
    digits = int(raw_input().strip())
    digits_arr = [int(d) for d in str(digits)]
    
    count = 0
    for digit in digits_arr: 
        
        if digit != 0:
            if (digits % digit == 0):
                count += 1
    
    print count
    
