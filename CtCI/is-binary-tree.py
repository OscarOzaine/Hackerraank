""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def get_inorder(node, result_nodes):
    if node == None:
        return None
    
    get_inorder(node.left, result_nodes)
    result_nodes.append(node.data)
    get_inorder(node.right, result_nodes)
    
    return result_nodes

def isBinarySearch(nodes):
        
    for i in range(0, len(nodes) - 2):
        if nodes[i] > nodes[i + 1] or nodes[i] == nodes[i + 1]:
            return False
    
    if nodes[len(nodes) - 2] > nodes[len(nodes) - 1] or nodes[len(nodes) - 2] == nodes[len(nodes) - 1]:
        return False
    
    return True

def check_binary_search_tree_(root):
    
    nodes = []
    result = get_inorder(root, nodes)
    
    if isBinarySearch(result) == True:
        return True
    else:
        return False
    
    