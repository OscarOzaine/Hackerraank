## Day 24: More Linked Lists
## https://www.hackerrank.com/challenges/30-linked-list-deletion

def removeDuplicates(self, head):
    start = head
    while start.next != None:
        if start.data == start.next.data:
            start.next = start.next.next
        else: 
            start = start.next
    return head
