
def climbingStaircase(n, k):
    result = stairs(n, k)
    print result
    '''
    for array in result:
        print (''.join(str(x) for x in array ) )
        
    '''
    
    
def stairs(n, k):
    array = []
    if n == 1:
        array.append([1])
    elif n == 2:
        tempArray = stairs(n-1, k)
        for temp in tempArray:
            array.append([1]+ temp)
            
        array.append([2])
    else:
        tempArray = stairs(n-1, k)
        for temp in tempArray:
            array.append([1]+ temp)

        tempArray = stairs(n-2, k)
        for temp in tempArray:
            array.append([2]+ temp)
        
            
    return array

    