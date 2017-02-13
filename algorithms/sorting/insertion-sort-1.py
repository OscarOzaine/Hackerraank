#Insertion Sort - Part 1
#https://www.hackerrank.com/challenges/insertionsort1

def insertionSort(ar):
    e = ar[len(ar) - 1]
    ar[len(ar) - 1] = ar[len(ar) - 2]
    print(' '.join(map(str, ar)))
    for x in range(len(ar) - 2, -1, - 1):
        if ar[x - 1] <= e or x == 0:
            ar[x] = e
            return ar
            
        else:
            ar[x] = ar[x - 1]
            print(' '.join(map(str, ar)))
    return ar

m = input()
ar = [int(i) for i in raw_input().strip().split()]
ar = insertionSort(ar)
print(' '.join(map(str, ar)))
