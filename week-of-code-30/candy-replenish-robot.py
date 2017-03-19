## Candy Replenishing Robot
## https://www.hackerrank.com/contests/w30/challenges/candy-replenishing-robot

def getCandies(bowl_size, candies, time):
    candysum = 0
    new_bowl_size = bowl_size
    x = 0
    time = range(0, time)
    
    for i in time:
        if new_bowl_size > candies[x]:
            new_bowl_size -= candies[x]
            
        if new_bowl_size < 5 and x < len(time) - 1:
            candysum += bowl_size - new_bowl_size
            new_bowl_size += (bowl_size - new_bowl_size)
            
        x += 1
        
    
    return candysum
    

n, t = raw_input().strip().split(' ')
n, t = [int(n), int(t)]
candies = map(int, raw_input().strip().split(' '))

print getCandies(n, candies, t)
