def findFirstSubstringOccurrence(s, x):
    
    f = s.find(x)
    if f >= 0:
        return f
    
    return -1
    