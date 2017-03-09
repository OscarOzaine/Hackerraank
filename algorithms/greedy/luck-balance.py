## Luck Balance
## https://www.hackerrank.com/challenges/luck-balance

N, K = map(int, raw_input().strip().split(' '))

priority = []
notpriority = []

for i in range(0, N):
    contest  = map(int, raw_input().strip().split(' '))
    if contest[1] == 1:
        priority.append(contest[0])
    else:
        notpriority.append(contest[0])
x = 0
thesum = 0

priority = sorted(priority, reverse=True)

for i in priority:
    if x < K:
        thesum += i
    else:
        thesum -= i
        
    x += 1

thesum += sum(notpriority)

print thesum
