
def countInversions(array, n):
	if n == 1:
		return 0
	else:
		left = array[:n/2]
		x = countInversions(array, n/2)
		right = array[n/2:]
		y = countInversions(array, n/2)
		z = countSplitInversions(array, left, right)
	return x + y + z

def countSplitInversions(array, left, right):
	i = 0
	j = 0
	count = 0
	while i < len(left) or j < len(right):

		if i == len(left):
			array[i+j] = right[j]
			j+=1
		elif j == len(right):
			array[i+j] = left[j]
			i+=1
		elif left[i] <= right[j]:
			array[i+j] = left[j]
			i+=1
		else:
			array[i+j] = right[j]
			count += len(left) - i
			j+=1

	return count


array = map(int, raw_input().strip().split(' '))

print array

print countInversions(array, len(array))
