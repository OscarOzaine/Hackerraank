import random

class TreeNode:
	data = None
	left = None
	right = None
	size = 0

	def __init__(self, data):
		self.data = data
		self.size = 1

	def getRandomNode(self):
		if self.left == None:
			leftSize = 0
		else:
			leftSize = self.left.size

		index = random.randint(0, self.size)
		
		if index < leftSize:
			return self.getRandomNode()
		elif index == leftSize:
			return self
		else:
			return self.getRandomNode(self.right)


	def insertInOrder(self, data):
		if data <= self.data:
			if self.left == None:
				self.left = TreeNode(data)
			else:
				self.left.insertInOrder(data)
		else:
			if self.right == None:
				self.right = TreeNode(data)
			else:
				self.right.insertInOrder(data)

		self.size += 1

	def size(self):
		return self.size

	def data(self):
		return self.data

	def find(self, data):
		if data == self.data:
			return self
		elif data <= self.data:
			if self.left != None:
				return self.left.find(data)
			else:
				return None
		elif data > self.data:
			if self.right != None:
				return self.right.find(data)
			else:
				return None

		return None



array = [5, 7, 2]
#array = sorted(array)
#node = createMinimalBST(array)

#node.insertArray(array)

node = TreeNode(5)
node.insertInOrder(7)
node.insertInOrder(2)

print node.data
print node.left.data
print node.right.data
print

random = node.getRandomNode()

if random != None:
	print random.data
print 
