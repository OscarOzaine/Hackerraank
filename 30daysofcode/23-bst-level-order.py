## Day 23: BST Level-Order Traversal
## https://www.hackerrank.com/challenges/30-binary-trees

def levelOrder(self, root):
    if root == None:
        return
    nodes = []
    nodes.append(root)
    
    while nodes:
        current = nodes.pop(0)
        print current.data,
        
        if current.left != None:
            nodes.append(current.left)
        
        if current.right != None:
            nodes.append(current.right)
    
	    