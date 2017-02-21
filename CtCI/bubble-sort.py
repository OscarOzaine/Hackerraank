#Sorting: Bubble Sort
##https://www.hackerrank.com/challenges/ctci-bubble-sort

def bubbleSort(array):
    len_array = len(array)
    numberOfSwaps = 0
    for i in range(0, len_array):
        
        for j in range(0, len_array - 1):
            if array[j] > array[j + 1]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
                numberOfSwaps += 1
    
        if numberOfSwaps == 0:
            break
    
    print 'Array is sorted in ' + str(numberOfSwaps) + ' swaps.'
    print 'First Element: ' + str(array[0])
    print 'Last Element: ' + str(array[len(array) - 1])
    
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

bubbleSort(a)
