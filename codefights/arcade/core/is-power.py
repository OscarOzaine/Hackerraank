def isPower(num):
    
    if num == 1:
        return True
    
    for i in range(0, num):
        for j in range(0, num):
            if i ** j == num:
                return True
            
    return False
            