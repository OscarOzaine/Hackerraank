class Solution(object):
    def isBalanced(self, root):

        return self.check(root) != -1

    def check(root):
        if root is None:
            return 0

        left  = self.check(root.left)
        right = self.check(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return 1 + max(left, right)
            
        