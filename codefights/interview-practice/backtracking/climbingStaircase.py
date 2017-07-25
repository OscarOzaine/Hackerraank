path = [0]*100
pp = []
def climbingStaircase(n, k):
    ss = 0
    idx = 0

    stairs(n, k, ss, idx)
    return pp
    
    
def stairs(n, k, ss, idx):
    if ss == n:
        p = []
        for i in range(0, idx):
            p.append(path[i])
            
        pp.append(p)
        return

    if ss > n:
        return
    
    if ss < n:
        for i in range(1, k+1):
            path[idx] = i
            stairs(n, k, ss + i, idx + 1)
            
