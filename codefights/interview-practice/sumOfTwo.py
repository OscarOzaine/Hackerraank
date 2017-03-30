'''
4
10 1 5 3 8
100 6 3 1 5


2
3 2 3 7 5 0 3 0 4 2
6 8 2 9 7 10 3 8 6 0

'''

## n log n
def sumOfTwo2(a, b, v):
    d = set(b)
    for ea in a:
        if abs(v - ea) in d:
            return True
        
    return False
    

## n**2
def sumOfTwo(a, b, v):
	lenA = len(a)
	lenB = len(b)

	i = 0
	j = lenB - 1
	a = sorted(a)
	b = sorted(b)
	while i < lenA:
		while lenB > 0:
			if a[i] + b[j] < v:
				break
			if a[i] + b[j] == v:
				return True
			j -= 1
			if j < 0:
				return False

		if a[i] + b[j] > v:
			break

		i += 1

	return False

v = int(raw_input().strip())

a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))

print sumOfTwo(a, b, v)
print sumOfTwo2(a, b, v)
