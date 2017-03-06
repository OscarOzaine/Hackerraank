## Minimal Tree
## Given a sorted array with unique integer elements, write an
## algorithm to create a binary search tree with minimal height

## Prints the depth of the Binary Search Tree

class TreeNode:
    left = None
    right = None
    data = None
    counter = None
    def __init__(self, data):
        self.data = data

def createMinimalBST(array):
    return _createMinimalBST(array, 0, len(array) - 1)

def _createMinimalBST(array, start, end, counter = 1):

    if end < start:
        return None

    mid = (start + end) / 2
    n = TreeNode(array[mid])
    n.depth = counter
    n.left = _createMinimalBST(array, start, mid - 1, counter + 1)
    n.right = _createMinimalBST(array, mid + 1, end, counter + 1)

    return n

def checkBalanced(root):
    if root == None:
        return -1

    leftHeight = checkBalanced(root.left)
    if leftHeight == -2:
        return -2

    rightHeight = checkBalanced(root.right)

    if rightHeight == -2:
        return -2

    heightDiff = leftHeight - rightHeight

    if abs(heightDiff) > 1:
        return -2
    else:
        return max([leftHeight, rightHeight]) + 1

def isBalanced(root):
    return checkBalanced(root) != -2

array = [1, 23, 5, 3, 2, 3, 1, 4, 4, 75]

result = createMinimalBST(array)

print isBalanced(result)
