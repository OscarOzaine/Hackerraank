def adjacentElementsProduct(inputArray):
    maxv = -5000
    
    for i in range(0, len(inputArray) - 2):
        product = int(inputArray[i]) * (inputArray[i + 1])
        if product > maxv:
            maxv = product
    
    product = int(inputArray[len(inputArray) - 2]) * (inputArray[len(inputArray) - 1])
    if product > maxv:
        maxv = product
            
    return maxv

array = map(int, raw_input().strip().split(' '))
print adjacentElementsProduct(array)
