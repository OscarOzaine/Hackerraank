## Day 22: Binary Search Trees
## https://www.hackerrank.com/challenges/30-binary-search-trees

def getHeight(self, root):
    if root == None:
        return -1
    
    left_height = self.getHeight(root.left)
    right_height = self.getHeight(root.right)
    
    return max([left_height, right_height]) + 1