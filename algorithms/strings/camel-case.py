##CamelCase 
##https://www.hackerrank.com/challenges/camelcase

import sys

string = raw_input().strip()
string = list(string)

words = 1
for s in string:
    
    if s.istitle():
        words += 1
    
print words
