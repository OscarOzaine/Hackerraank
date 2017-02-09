#!/bin/python
#Insert a node at a specific position in a linked list
#Hackerrank.com

"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def InsertNth(head, data, position):
    node = Node()
    node.data = data
    temp = head
    prev = Node()
    
    if position == 0:
        node.next = head
        head = node
        return head
    else:
        
        while position > 0:
            prev = temp
            temp = temp.next
            position -= 1
            
        prev.next = node
        node.next = temp
        return head
    