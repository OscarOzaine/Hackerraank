## Priyanka and Toys
## https://www.hackerrank.com/challenges/priyanka-and-toys

N = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

arr = sorted(arr)
x = 0
count = 1

x = 0
comparator = arr[0]
for i in arr:
    if x == len(arr) - 1:
        if not (arr[x] >= comparator and arr[x] <= comparator + 4):
            comparator = arr[x]
            count += 1
        break
        
    #print arr[x]
    if not (arr[x] >= comparator and arr[x] <= comparator + 4):
        comparator = arr[x]
        count += 1
        
    x += 1
    
print count
