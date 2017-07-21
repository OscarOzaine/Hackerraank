def containsDuplicates(a):
    s = {}
    for i in a:
        if i not in s:
            s[i] = 1;
        else:
            return True
        
    return False
        

