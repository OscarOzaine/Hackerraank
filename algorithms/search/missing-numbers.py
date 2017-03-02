## Missing Numbers
## https://www.hackerrank.com/challenges/missing-numbers

a_n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

b_n = int(raw_input().strip())
b = map(int, raw_input().strip().split(' '))

def findDifference(sorted_a, sorted_b):
    diff = []
    for itemB in sorted_b:
        if itemB in sorted_a:
            if sorted_b[itemB] > sorted_a[itemB]:
                diff.append(itemB)
        else:
            diff.append(itemB)
            
    return diff

sorted_a = {}
a = sorted(a)
for i in a:
    if sorted_a.get(i, False):
        sorted_a[i] += 1
    else:
        sorted_a[i] = 1

sorted_b = {}
b = sorted(b)
for i in b:
    if sorted_b.get(i, False):
        sorted_b[i] += 1
    else:
        sorted_b[i] = 1
        
diff = findDifference(sorted_a, sorted_b)

for i in diff:
    print i,
