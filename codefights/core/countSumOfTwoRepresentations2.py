def countSumOfTwoRepresentations2(n, l, r):
    if l > n / 2:
        return 0
    
    m = 0
    if n % 2 != 1:
        m = 1
        
    return min(n / 2 - l, r - n / 2) + m

def countSumOfTwoRepresentations2Loop(n, l, r):
    res = 0
    counter = 0
    for i in range(l, r+1):
        b = n - i
        if b >= l and b <= r and b >= i:
            counter += 1
    
    return counter
    

