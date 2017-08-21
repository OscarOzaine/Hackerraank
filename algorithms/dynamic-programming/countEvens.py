
def countEvens(string, index = 1, counter = 0):
    if index == len(string):
        return counter
        
    if int(string[index]) % 2 == 0:
        return countEvens(string, index+1, counter+1)
    
    return countEvens(string, index+1, counter)


ss = '574674546476'

for i in range(0, len(ss)):
    print countEvens(ss, i),
    

