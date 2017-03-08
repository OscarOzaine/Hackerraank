## Grid Challenge
## https://www.hackerrank.com/challenges/grid-challenge

def isPossibleArrange(matrix):
    
    for i in range(0, len(matrix) - 1):
        sorted_arr = sorted(G[i])
        x = 0
        letters = [chr(i) for i in sorted_arr]
        
        for j in sorted_arr:
            
            if x < len(sorted_arr) - 1:
                
                if sorted_arr[x] > sorted_arr[x + 1]:
                    return 'NO'
            else:
                if sorted_arr[x - 1] > sorted_arr[x]:
                    return 'NO'
            
            x += 1
            
    sums = []
    for i in matrix:
        if i == len(matrix) - 1:
            break
        
        if sum(matrix[i]) > sum(matrix[i + 1]) or min(matrix[i]) > min(matrix[i + 1]):
            return 'NO'
        
    return 'YES'
    

T = int(raw_input().strip())

for i in range(0, T):
    N = int(raw_input().strip())
    
    G = {}
    for x in range(0, N):
        letters = list(raw_input().strip())
        letters = [ord(i) for i in letters]
        G[x] = letters
        
    print isPossibleArrange(G)