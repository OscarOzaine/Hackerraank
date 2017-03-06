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

def getHeight(root):
    if root == None:
        return -1

    return max([getHeight(root.left), getHeight(root.right)]) + 1

def checkBalanced(root):
    if root == None:
        return True

    height = getHeight(root.left) - getHeight(root.right)
    if abs(height) > 1:
        return False
    else:
        return checkBalanced(root.left) and checkBalanced(root.right)
    
array = [5, 2, 8, 4, 5, 6, 7, 8, 9]

result = createMinimalBST(array)
print checkBalanced(result)
