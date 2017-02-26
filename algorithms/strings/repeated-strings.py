## Repeated String
## https://www.hackerrank.com/challenges/repeated-string

def countLetters(string, n):
    count = 0
    letterCount = 0
    
    if n <= len(string):
        x = 0
        for s in string:
            if x == n:
                return letterCount
            
            if s == 'a':
                letterCount += 1
            x += 1

    for s in string:
        if s == 'a':
            letterCount += 1
    
    res = (n / len(string))
    
    
    count += res * letterCount
    
    if n % len(string) > 0:
        x = 0
        for s in string:
            if n % len(string) == x:
                break
                
            if s == 'a':
                count += 1
                
            x += 1
        
    return count

string = raw_input().strip()
n = long(raw_input().strip())

print countLetters(string, n)
