#Day 6: Let's Review

n = raw_input().strip()

for i in range(0, int(n)):
    
    
    string = raw_input().strip()
    string = list(string)
    
    pair = []
    notpair = []
    index = 0
    for j in string:
        if index % 2 == 0:
            pair.append(string[index])
        else:
            notpair.append(string[index])
        index += 1
            
    
    print str(''.join(pair)) + ' ' + str(''.join(notpair))
    
