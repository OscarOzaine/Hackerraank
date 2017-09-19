'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \\
     2
    //
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

'''


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def inorderTraversal(self, root, result=[]):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if root.left != None:
			self.inorderTraversal(root.left, result)

		result.append(root.val)

		if root.right != None:
			self.inorderTraversal(root.right, result)

		return result


s = Solution()

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

res = s.inorderTraversal(root)    
print res    