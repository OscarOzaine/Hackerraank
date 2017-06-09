d = [0] * 21
def fibonacciModified(a, b, n):
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        if d[n] > 0:
            return d[n]
        else:
            d[n] = fibonacciModified(a, b, n - 1) * fibonacciModified(a, b, n - 1) + fibonacciModified(a, b, n - 2)
            return d[n]
        
a, b, n = map(int, raw_input().strip().split())

print fibonacciModified(a, b, n)
