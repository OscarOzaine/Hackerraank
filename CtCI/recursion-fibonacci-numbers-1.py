#Recursion: fibonacci numbers
##https://www.hackerrank.com/challenges/ctci-fibonacci-numbers

def fibonacci(n, count = 1, old_val = 0, new_val = 1):
    
    while n >= count:
        temp = old_val
        old_val = new_val
        new_val += temp
        return fibonacci(n, count + 1, old_val, new_val)
    
    return old_val
    
    
n = int(raw_input().strip())

print fibonacci(n)
