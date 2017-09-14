
def permuteIterative(array):
	permutations = [[]]
	for a in array:
		new_perms = []
		for perm in permutations:
			
			for i in xrange(len(perm) + 1):
				new_perms.append(perm[:i] + [a] + perm[i:])
			

		permutations = new_perms

	#print permutations
	return permutations

def permutateDFS(nums):
	result = []
	result = dfs(nums, len(nums), [], result)

	print result


def dfs(nums, level, path, result):
	if level == 0:
		result.append(path)
		return

	for i in range(0, len(nums)):
		if nums[i] not in path:
			dfs(nums, level - 1, path + [nums[i]], result)

	return result

def permuteRecursive(num):
    return _permuteRecursive(num)


def _permuteRecursive(num):
    if len(num) == 1:
        return [num]

    if len(num) == 2:
        return [[num[0], num[1]], [num[1], num[0]]]

    ret = []
    for i in xrange(len(num)):
        _ret = _permuteRecursive(num[:i] + num[i+1:])
        for one in _ret:
        	ret.extend([[num[i]] + one for one in _ret])

    return ret

array = [1, 2, 3]

print permuteIterative(array)

print

print permuteRecursive(array)

print 

print permutateDFS(array)
