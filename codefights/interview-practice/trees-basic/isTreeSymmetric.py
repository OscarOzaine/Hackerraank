#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def isTreeSymmetric(t, val = 0):

    return isMirror(t, t)

def isMirror(root1 , root2):
    
    if root1 is None and root2 is None:
        return True

    """ 
    For two trees to be mirror images, the following three conditions must be true
    1 - Their root node's key must be same
    2 - left subtree of left tree and right subtree of right tree have to be mirror images
    3 - right subtree of left tree and left subtree of right tree have to be mirror images
    """
    if (root1 is not None and root2 is not None):
        if root1.value == root2.value:
            return (isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left))
            
    # If neither of above conditions is true then root1
    # and root2 are not mirror images

    return False