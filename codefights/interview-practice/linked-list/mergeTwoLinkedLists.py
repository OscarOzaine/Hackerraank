# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    
    result = []
    if l1 != None and l2 != None:
        
        if l1.value <= l2.value:
            result.append(l1.value)
            l1 = l1.next
        else:
            result.append(l2.value)
            l2 = l2.next
    
    while l1 != None or l2 != None:
        
        
        if l1 != None and l2 != None:
            
            if l1.value <= l2.value:
                result.append(l1.value)
                l1 = l1.next
            elif l1.value > l2.value:
                result.append(l2.value)
                l2 = l2.next
            elif l1 == None and l2 != None:
                l2 = l2.next
                result.append(l2.value)
            elif l2 == None and l1 != None:
                l1 = l1.next
                result.append(l1.value)
                
        elif l1 != None:
            result.append(l1.value)
            l1 = l1.next
        elif l2 != None:
            result.append(l2.value)
            l2 = l2.next
            

    return result

