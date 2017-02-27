## Viral Advertising
## https://www.hackerrank.com/challenges/strange-advertising

n = int(raw_input().strip())

people = 5
share = 0
ads = 0

for i in range(0, n):
    share = people / 2
    people = share * 3
    ads += share
    
print ads
    