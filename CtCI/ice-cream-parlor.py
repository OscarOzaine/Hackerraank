## Binary Search: Ice Cream Parlor
## https://www.hackerrank.com/challenges/ctci-ice-cream-parlor

t = int(raw_input().strip())

for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    array = map(int, raw_input().strip().split(' '))

    match = False
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue
            
            if array[i] + array[j] == m:
                match = True
                if i > j:
                    mi = j + 1
                else:
                    mi = i + 1
                
                if i > j:
                    mx = i + 1
                else:
                    mx = j + 1
            
                print str(mi) + ' ' + str(mx)
                
        if match == True:
            break
        