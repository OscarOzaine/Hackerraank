

def binarySearch(arr, item):
	found = False
	bottom = 0
	top = len(arr)-1
	while bottom < top and not found:
		middle = bottom + top / 2

		if arr[middle] == item:
			found = True
		elif arr[middle] < item:
			bottom = middle + 1
		else:
			top = middle - 1

	return found


def binarySearchCount(arr, item):
	found = False
	counter = 0
	bottom = 0
	top = len(arr)-1
	while bottom < top and not found:
		counter+=1
		middle = bottom + top / 2

		if arr[middle] == item:
			found = True
		elif arr[middle] < item:
			bottom = middle + 1
		else:
			top = middle - 1

	return counter

#Ordered list
arr = [2, 5, 7, 12, 14, 21, 28, 31, 36]

print binarySearch(arr, 5)
print binarySearchCount(arr, 5)

