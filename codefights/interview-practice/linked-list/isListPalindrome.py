# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    vals = []
    while l:
        vals.append(l.value)
        l = l.next
    
    return vals == vals[::-1]
        

