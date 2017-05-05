# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root, summ = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
            
        
        if root.left is not None and root.right is not None:
            summ += self.findTilt(root.left, summ)
            summ += self.findTilt(root.right, summ)
            summ += abs(root.left.val - root.right.val)
        elif root.left is not None:
            summ += self.findTilt(root.left, summ)
            summ += root.left.val
        elif root.right is not None:
            summ += self.findTilt(root.right, summ)
            summ += root.right.val
        
        
        return summ
        
        