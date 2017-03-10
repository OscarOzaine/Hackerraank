import math

tests = int(raw_input().strip())


for t in range(tests):
    
    N, M, ID = map(int, raw_input().strip().split(' '))

    last = ((M - 1) + (ID - 1)) % N + 1
    print last
    