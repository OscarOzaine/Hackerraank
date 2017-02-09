"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if head == None:
        return
    
    temp = head
    
    if position == 0:
        head = temp.next
        temp = None
        return head
    
    for i in range(position - 1):
        temp = temp.next
        if temp == None:
            break
    
    if temp == None:
        return
    if temp.next == None:
        return
    
    next = temp.next.next
    temp.next = None
    temp.next = next
    
    return head
    
  
