
def factorial(n, factorial_sum = 1):
    factorial_sum = (n * factorial_sum)
    
    if n <= 2:
        return factorial_sum
    
    return factorial(n - 1, factorial_sum)
    
    
n = int(raw_input().strip())

print factorial(n)