##Day 15: Linked List
##https://www.hackerrank.com/challenges/30-linked-list

def insert(self, head, data): 
    node = Node(data)
    
    if head == None:
        self.head = node
        self.next = None
    else:
        headt = self.head
        while headt.next != None:
            headt = headt.next
        headt.next = node
        headt.next.next = None
        
    return self.head
