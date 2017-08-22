
def maxSubarrayContiguous(array, indexMax):
	maxSoFar = array[0]
	currMax = array[0]

	for i in range(1, indexMax):
		currMax = max(array[i], currMax + array[i])
		maxSoFar = max(maxSoFar, currMax)

	return maxSoFar

def maxSubarrayNonContiguous(array, indexMax):
	sumMax = 0
	maxx = array[0]
	negArray = True
	res = 0

	for i in range(indexMax):

		if array[i] >= 0:
			sumMax += array[i]
			negArray = False

		if array[i] >= maxx:
			maxx = array[i]
            
	if negArray == False:
		res = sumMax

	if negArray:
		res = maxx

	return res




n = int(raw_input())

for i in range(n):
    nn = int(raw_input())
    ss = map(int, raw_input().split())
    
    print maxSubarrayContiguous(ss, len(ss)), maxSubarrayNonContiguous(ss, len(ss))