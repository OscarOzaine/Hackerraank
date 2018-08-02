
def twoSum(arr, num):
	sums = []
	for x in range(len(arr)):
		for y in range(len(arr)):

			if ((arr[x] + arr[y] == num) and ([arr[y], arr[x]] not in sums)):
				sums.append([arr[x], arr[y]])

	return sums


def twoSum2(arr, s):
	sums = []
	hashmap = {}
	for x in range(len(arr)):
		suMinus = s - arr[x]

		if (suMinus in hashmap):
			sums.append([hashmap[suMinus], arr[x]])

		hashmap[arr[x]] = arr[x]

	return sums

print(twoSum([3, 5, 2, -4, 8, 11], 7))

print(twoSum2([3, 5, 2, -4, 8, 11], 7))
