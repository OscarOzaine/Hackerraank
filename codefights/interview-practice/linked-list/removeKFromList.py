# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    
    res = []
    
    while l:
        
        if l.value != k:
            res.append(l.value)
        l = l.next
        
    return res
    

