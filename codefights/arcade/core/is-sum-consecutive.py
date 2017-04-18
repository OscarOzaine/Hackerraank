def isSumOfConsecutive2(n):
    numbers = range(1, n+1)
    
    x=1
    counter = 0
    for i in numbers:
        
        nums = numbers[x:]
        ss = i
        for j in (nums):
            ss += j
            if ss == n:
                counter += 1
                break
            elif ss > n:
                break
        x += 1
    return counter
