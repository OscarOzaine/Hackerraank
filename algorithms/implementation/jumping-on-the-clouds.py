## Jumping on the Clouds
## https://www.hackerrank.com/challenges/jumping-on-the-clouds


n = int(raw_input().strip())
clouds = map(int,raw_input().strip().split(' '))

count = 0
x = 0

while x < len(clouds) - 2:
    
    if clouds[x + 2] == 0:
        count += 1
        x += 2
    elif clouds[x + 2] == 1 and clouds[x + 1] == 0:
        count += 1
        x += 1
    elif clouds[x + 1] == 1:
        break
        
if x == len(clouds) - 2:
    count += 1

print count
