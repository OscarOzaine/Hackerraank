## Recursion: Davis' Staircase
## https://www.hackerrank.com/challenges/ctci-recursive-staircase

def getSteps(n, cache=dict()):
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    total = 0
    if cache.get(n):
        return cache[n]
    
    for hop in [1, 2, 3]:
        total += getSteps(n-hop, cache)
        cache[n] = total
        
    return cache[n]
    
s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print getSteps(n)
    
