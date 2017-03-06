## 4.5 Validate BST
## Implement a function to check if a binary tree is a binary search tree.
## Min/Max Solution
## Leverage the solution of the binary search
## left.data <= current.data < right.data

class TreeNode:
    left = None
    right = None
    data = None
    counter = None
    def __init__(self, data):
        self.data = data

def checkBST(root):
	return _checkBST(root, None, None)

def _checkBST(root, minimum, maximum):

	if root == None:
		return True

	if ((minimum != None and root.data <= minimum) or (maximum != None and root.data > maximum)):
		return False

	if not _checkBST(root.left, minimum, root.data) or not _checkBST(root.right, root.data, maximum):
		return False

	return True

#Not Balanced
node = TreeNode(10)
node.left = TreeNode(20)
node.right = TreeNode(10)
print checkBST(node)

#Balanced
node = TreeNode(10)
node.left = TreeNode(5)
node.right = TreeNode(15)

print checkBST(node)
