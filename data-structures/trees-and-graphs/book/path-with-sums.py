


## Brute Force
def countPathWithSum(root, targetSum):
	if root == None:
		return 0

	pathsFromRoot = _countPathWithSum(root, targetSum, 0)
	pathsOnLeft = countPathWithSum(root.left, targetSum)
	pathsOnRight = countPathWithSum(root.right, targetSum)

	return pathsFromRoot + pathsOnLeft + pathsOnRight


def _countPathWithSum(node, targetSum, currentSum):
	if node == None:
		return 0

	currentSum += node.data

	totalPaths = 0
	if currentSum == targetSum:
		totalPaths += 1

	totalPaths += _countPathWithSum(node.left, targetSum, currentSum)
	totalPaths += _countPathWithSum(node.right, targetSum, currentSum)
	
	return totalPaths




## Optimized

def countPathWithSum2(node, targetSum):
	pathCount = {}
	return _countPathWithSum2(root, targetSum, 0, pathCount)

def _countPathWithSum2(node, targetSum, runningSum, pathCount):
	if node == None:
		return 0

	runningSum += node.data
	summ = runningSum - targetSum
	totalPaths = pathCount.get(sum, 0)

	if runningSum == targetSum:
		totalPaths += 1

	incrementHashTable(pathCount, runningSum, 1)
	totalPaths += _countPathWithSum2(node.left, targetSum, runningSum, pathCount)
	totalPaths += _countPathWithSum2(node.right, targetSum, runningSum, pathCount)
	incrementHashTable(pathCount, runningSum, -1)

	return totalPaths

def incrementHashTable(hashTable, key, delta):
	newCount = hashTable.get(key, 0) + delta
	if newCount == 0:
		hashTable.remove(key)
	else:
		hashTable[key] = newCount

	return hashTable

