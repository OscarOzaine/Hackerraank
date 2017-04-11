def firstDuplicate(a):
    d = {}
    x=0
    res = {}
    mm = max(a)
    val = 0
    
    for i in a:
        
        if d.get(i) == None:
            d[i] = []
            d[i].append(x)
        else:
            d[i].append(x)
            
        if len(d[i]) > 1:
            res[i] = x
            if x <= mm:
                mm = x
                val = i
        x+=1
    
    if len(res) == 0:
        return -1
    
    return val
    