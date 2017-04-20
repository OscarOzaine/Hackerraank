def pagesNumberingWithInk(current, numberOfDigits):
    
    n = list(str(current))
    
    while numberOfDigits >= len(n):
        n = list(str(current))
        numberOfDigits -= len(n)
        current += 1
        
        
    return current - 1

