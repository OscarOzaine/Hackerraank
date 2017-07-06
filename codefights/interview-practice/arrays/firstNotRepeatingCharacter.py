def firstNotRepeatingCharacter(s):
    if len(s) == 1:
        return s
        
    counter = {}
    result = []
    for i in range(len(s)):
        if s[i] not in counter:
            
            counter[s[i]] = 1
            result.append(s[i])
        else:
            counter[s[i]] += 1
            if s[i] in result:
                result.remove(s[i])
    
    if len(result) > 0:
        return result[0]
    
    return '_'
    
            
            
    
        

