def containsCloseNums(nums, k):
    
    
    thenums = []
    s = 0
    for i in nums:
        thenums.append([i,s])
        s+=1
        
    thenums = sorted(thenums, key=lambda i:i[0])
    for i in range(1, len(thenums)):
        if thenums[i][0] == thenums[i-1][0]:
            if thenums[i][1] - thenums[i-1][1] <= k:
                return True
            
    return False
