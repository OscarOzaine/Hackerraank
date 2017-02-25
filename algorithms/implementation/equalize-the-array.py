##Equalize the Array 
##https://www.hackerrank.com/challenges/equality-in-a-array

import sys
n = raw_input().strip()
array = raw_input().strip().split(' ')

max_occurrences = 0
for s in array:
    counts = array.count(s)
    if counts >= max_occurrences:
        max_occurrences = counts
        
print len(array) - max_occurrences
