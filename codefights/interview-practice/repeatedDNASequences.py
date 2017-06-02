def repeatedDNASequences(s):
    seen = {}
    tt = []
    for i in range(0, len(s)-2):
        if s[i:i+10] in seen and s[i:i+10] not in tt:
            tt.append(s[i:i+10])
        else:
            seen[s[i:i+10]] = 1
            
    
    return sorted(tt)
    
