def reverseInteger(x):
    revers = ''
    x = str(x)
    if int(x) >= 0:
        for i in range(len(x) - 1, -1, -1):
            revers += x[i]
        return int(revers)
    else:
        for i in range(len(x) - 1, 0, -1):
            revers += x[i]
            
        return int(revers)*-1
    
    return 0
    