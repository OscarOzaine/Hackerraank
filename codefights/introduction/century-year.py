def centuryFromYear(year):
    
    y = str(year)
    if len(y) == 1 or len(y) == 2:
        return 1
    
    n = int(y[len(y) - 1] + y[len(y) - 1])
    
    if len(y) == 3:
        y = y[0]
    else:
        y = y[0] + y[1]
              
    if n > 0 and n < 100:
        
        return int(y) + 1
    
    return int(y)





n = raw_input().strip()


print centuryFromYear(n)
