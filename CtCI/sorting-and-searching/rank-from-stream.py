# Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a number x
# Implement the data structures and algoritghms to support these operations, implementh method track(int x) when each number is genetated
# and the method getRankOfNumber(int x), returns the number of values less than or equal to x

# Example:
# Stream (In order of appearence): 5, 1, 4, 4, 5, 9, 7, 13, 3
# getRankOfNumber(1) = 0
# getRankOfNumber(3) = 1
# getRankOfNumber(4) = 3


root = None

def track(number):
	if root == None:
		root = RankNode(number)
	else:
		root.insert(number)

def getRankOfNumber(number):
	return root.getRank(number)

class RankNode:
	left_size = 0
	left = None
	right = None
	data = 0

	def __init__(self, data):
		self.data = data

	def insert(self, d):
		if d <= self.data:
			if self.left != None:
				self.left.insert(d)
			else:
				self.left = RankNode(d)
			self.left_size+=1
		else:
			if self.right != None:
				self.right.insert(d)
			else:
				self.right = RankNode(d)

	def getRank(self, d):
		if d == self.data:
			return self.left_size
		elif d < self.data:
			if self.left == None:
				return -1
			else:
				return self.left.getRank(d)
		else:
			if self.right == None:
				right_rank = -1
			else:
				right_rank = self.right.getRank(d)

			if right_rank == -1:
				return -1
			else:
				return self.left_size + 1 + right_rank



arr = [5, 1, 4, 4, 5, 9, 7, 13, 3]
arr = sorted(arr)

mid = len(arr) / 2
root = RankNode(arr[mid])

del arr[mid]
for i in range(len(arr)):
	root.insert(i)

print root.getRank(1)
print root.getRank(3)
print root.getRank(4)
#root = arrayToBst(arr, 0, len(arr)-1)
