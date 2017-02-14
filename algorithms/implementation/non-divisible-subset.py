#Non Divisible Subset
#https://www.hackerrank.com/challenges/non-divisible-subset

n, k = map(int,raw_input().split())

numbers = map(int, raw_input().split())
print numbers
setFiltered = map(lambda x: x % k, numbers)

count = 0
print setFiltered
if 0 in setFiltered:
    count += 1

for num in xrange(1, (k // 2) + 1):
    if num == (k - num):
        if num in setFiltered:
            count += 1
    else:
        count1, count2 = 0, 0
        for numFiltered in setFiltered:                  
            if numFiltered == num:
                count1 += 1
            elif numFiltered == (k - num):
                count2 += 1
        count += max(count1, count2)
print count
