def sumN(x):
	ss = 0
	b = 1
	if n <= 0:
		b = n
		x = 1

	for i in range(b, x + 1):
		ss += i

	return ss

n = int(raw_input().strip())

print sumN(n)
