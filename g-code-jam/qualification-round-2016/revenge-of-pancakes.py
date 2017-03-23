import sys

def countHappy(pancakes):
	counter = 0
	for i in range(1, len(pancakes)):
		if pancakes[i] != pancakes[i-1]:
			counter += 1

	if pancakes[-1] == "+":
		return counter
	else:
		return counter + 1


orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

n = int(raw_input().strip())

for i in range(n):
	pancakes = raw_input().strip()
	pancakes = list(pancakes)
	print 'Case #' + str(int(i) + 1) + ': ' + str(countHappy(pancakes))


sys.stdout = orig_stdout
f.close()