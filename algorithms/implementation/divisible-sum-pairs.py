## Divisible Sum Pairs
## https://www.hackerrank.com/challenges/divisible-sum-pairs

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
a = map(int, raw_input().strip().split(' '))
b = a

count = 0

for i in range(0, len(a)):
    for j in range(i, len(a)):
        s = a[i] + a[j]
        if s % k == 0 and i < j:
            count += 1

print count

