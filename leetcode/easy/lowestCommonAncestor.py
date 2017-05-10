# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def lowestCommonAncestor(root, p, q):
	if p.val < root.val and q.val < root.val:
		return lowestCommonAncestor(root.left, p, q)
	if p.val > root.val and q.val > root.val:
		return lowestCommonAncestor(root.right, p, q)

	return root

node = TreeNode(6)
node.left = TreeNode(2)
node.left.left = TreeNode(0)
node.left.right = TreeNode(4)
node.left.right.left = TreeNode(3)
node.left.right.right = TreeNode(5)

node.right = TreeNode(8)
node.right.left = TreeNode(7)
node.right.right = TreeNode(8)

print lowestCommonAncestor(node, node.left, node.left.right).val