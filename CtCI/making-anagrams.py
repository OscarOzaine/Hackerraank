#Strings: Making Anagrams
#Hackerrank.com

def number_needed(a, b):
    count = 0
    
    pos1 = range(0, 26)
    pos2 = range(0, 26)
    
    ind = 0
    for x in range(0, len(a)):
        ind = sum(bytearray(a[x])) - sum(bytearray('a'))
        pos1[ind] += 1
        
    for x in range(0, len(b)):
        ind = sum(bytearray(b[x])) - sum(bytearray('a'))
        pos2[ind] += 1
        
    for x in range(0, 26):
        count += abs(pos1[x] - pos2[x])
    
    return count

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
