def squareDigitsSequence(a0, occurrences = []):
    
    if a0 in occurrences:
        return len(occurrences) + 1
    
    occurrences.append(a0)
    
    num = map(int, list(str(a0)))
    s = 0
    for i in num:
        s+= (i**2)
        
    return squareDigitsSequence(s, occurrences)    
    

