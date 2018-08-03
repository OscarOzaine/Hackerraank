
class TreeNode:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data


def mergeTrees(t1, t2):

	if (t1 == None and t2 == None):
		return None

	if (t1 != None and t2 != None):
		t1.left = mergeTrees(t1.left, t2.left)
		t1.right = mergeTrees(t1.right, t2.right)
		t1.data += t2.data
		return t1

	if (t2 != None):
		return t2

	return t1

def inOrder(t, sums = []):

	if t == None:
		return t

	inOrder(t.left, sums)
	sums.append(t.data)
	inOrder(t.right, sums)

	return sums

def preOrder(t, sums = []):

	if t == None:
		return t

	sums.append(t.data)
	preOrder(t.left, sums)
	preOrder(t.right, sums)
	
	return sums

def postOrder(t, sums = []):

	if t == None:
		return t

	postOrder(t.left, sums)
	
	postOrder(t.right, sums)
	sums.append(t.data)
	
	return sums

t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)


t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(3)
t2.right.right = TreeNode(3)


print(preOrder(t1))

print(inOrder(t1))

print(postOrder(t1))

res = mergeTrees(t1, t2)



