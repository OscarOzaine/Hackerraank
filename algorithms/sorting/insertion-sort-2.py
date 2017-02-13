def insertionSort(ar, q):
    
    for i in range(q):
        if ar[q] < ar[i]:
            temp = ar[q]
            ar[q] = ar[i]
            ar[i] = temp
            
    return ar
    
m = input()
ar = [int(i) for i in raw_input().strip().split()]

for q in range(1, len(ar)):
    ar = insertionSort(ar, q)
    print(' '.join(map(str, ar)))

