## Bon Appetit
## https://www.hackerrank.com/challenges/bon-appetit

n, k = map(int, raw_input().strip().split(' '))
arr = map(int, raw_input().strip().split(' '))
charged = int(raw_input().strip())

arr.pop(k)
real = sum(arr) / 2
s = charged - real

if s != 0:
    print s
else:
    print 'Bon Appetit'
