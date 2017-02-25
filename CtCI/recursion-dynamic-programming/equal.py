
##Equal 
##https://www.hackerrank.com/challenges/equal
##Study change-making-problem
##Study coin-problem
import sys

def equal(temp):

    x = 0
    if temp >= 5:
        x = temp / 5
        temp = temp % 5

    if temp >= 2:
        x += temp / 2
        temp = temp % 2

    x += temp
    return x


def array_smallest(array, leng):

    smallest = sys.maxsize
    
    for i in range(0, leng):
        if not array.get(i):
            return smallest
        
        if array[i] < smallest:
            smallest = array[i]

    return smallest


t = int(raw_input().strip())

while(t):
    
    minv = 1000000;
    n = int(raw_input().strip())
    array = map(int, raw_input().strip().split(' '))
    
    for a in array:
        if a < minv:
            minv = a
            
    sumv = dict()
    for j in range(0, 5):
        sumv[j] = 0

        for i in range(0, n):
            mod = 0
            mod = array[i] - (minv - j)

            if mod > 0:
                temp = mod
            else:
                temp = (-1) * mod
            
            sumv[j] = sumv[j] + equal(temp)

    t -= 1
    print array_smallest(sumv, n)
