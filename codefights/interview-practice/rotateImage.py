def rotateImage(a):
    x = len(a) - 1
    y = 0
    res = [[] for i in range(0, len(a))]
    
    for i in range(0, len(a)):
        
        for j in range(0, len(a)):
            res[i].append(a[x][y])
            x-=1
            
        x = len(a) - 1
        y += 1
    
    return res
