#!/bin/python
#2D Array - DS
#Hackerrank.com
import sys

def getHourGlass(arr, external_row, external_field):
    sum = 0
    
    for row in range(external_row, external_row + 3):
        for field in range(external_field, external_field + 3):
            if row == external_row + 1 and field == external_field + 1:
                sum += arr[row][field]
            elif row != external_row + 1:
                sum += arr[row][field]
        field = external_field

    return sum

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)


sums = []
for row in range(0,4):
    for field in range(0,4):
        sums.append(getHourGlass(arr, row, field))
        
print max(sums)
