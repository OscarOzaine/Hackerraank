## Problem A. Counting Sheep
## https://code.google.com/codejam/contest/dashboard?c=6254486

import sys

def getNumber(n):
	counter = 1
	numbers = []
	x = 2
	new_n = n
	while len(numbers) <= 9:
		if n == 0:
			return 'INSOMNIA'
		
		nn = list(str(new_n))
		
		for i in set(nn):
			if i not in numbers:
				numbers.append(i)

		counter += 1
		new_n = int(n) * x
		x += 1

	return ''.join(map(str, nn))

n = int(raw_input().strip())

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

for i in range(n):
	inputC = int(raw_input().strip())
	number = getNumber(inputC)
	print 'Case #' + str(i + 1) + ': ' + str(number)
	

sys.stdout = orig_stdout
f.close()