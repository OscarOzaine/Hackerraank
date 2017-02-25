##Sock Merchant
##https://www.hackerrank.com/challenges/sock-merchant

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

count = 0
number_count = 0
while len(arr) > 1:
    number_count = 0
    
    first = arr[0]
    number_count = arr.count(first)
    
    if number_count >= 2:
        count += number_count / 2
    
    new_arr = []
    for i in arr:
        if i != first:
            new_arr.append(i)
    arr = new_arr
    
    
    
print count