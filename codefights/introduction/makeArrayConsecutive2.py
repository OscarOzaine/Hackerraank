def makeArrayConsecutive2(statues):
    
    mx = max(statues)
    mi = min(statues)
    
    c = 0
    for i in range(mi, mx):
        if i not in statues:
            c += 1
            
    return c

array = map(int, raw_input().strip().split(' '))
print makeArrayConsecutive2(array)
