from math import factorial as fact

def nChooseR(n, r):
    
    return fact(n) / ((fact(n - r) * fact(r)))
 
def goodStringsCount(n):

    return nChooseR(26, n) * (2**n - n - 1)
 