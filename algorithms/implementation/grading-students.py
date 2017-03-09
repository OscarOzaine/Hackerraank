## Grading Students
## https://www.hackerrank.com/challenges/grading

import sys

n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    
    if grade >= 38:
        remainder = grade % 5
        if remainder == 0:
            print grade
        else:
            if (grade + 5 - remainder) - grade < 3:
                print grade + 5 - remainder
            else:
                print grade
    else:
        print grade
        
