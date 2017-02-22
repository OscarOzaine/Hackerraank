#Recursion: fibonacci numbers - optimal
##https://www.hackerrank.com/challenges/ctci-fibonacci-numbers

def fibonacci(n):
    
    if n==1 or n==2:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(raw_input().strip())

print fibonacci(n)
