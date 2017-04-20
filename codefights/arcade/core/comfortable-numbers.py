def comfortableNumbers(L, R):
    if L == R:
        return 0
    
    a = L
    b = a + 1
    sumA = 0
    pairs = 0
    
    listPairs = []
    while a < R:
        aStr = str(a)
        aX = 0
        
        while aX < len(aStr):
            sumA = sumA + int(aStr[aX])
            aX = aX + 1
            
        while b<=R:
            bStr = str(b)
            bX = 0
            sumB = 0
            
            while bX < len(bStr):
                sumB = sumB + int(bStr[bX])
                bX = bX + 1
                
            if (b >= a - sumA) and (b <= a + sumA) and (a >= b - sumB) and (a <= b + sumB):
                pairs = pairs + 1
                
            b = b + 1;
                
        a = a + 1
        b = a + 1
        sumA = 0
                
            
    return pairs