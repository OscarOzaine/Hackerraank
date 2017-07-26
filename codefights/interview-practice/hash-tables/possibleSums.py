def possibleSums(coins, quantity):
    A = set([0])
    
    for val, cnt in zip(coins, quantity):

        B = set()
        for x in A:
            for y in range(0, val * cnt + 1, val):
                
                B.add(x + y)
        
        A = B
    
    return len(A) - 1


print possibleSums([10, 50, 100], [1, 2, 1])
