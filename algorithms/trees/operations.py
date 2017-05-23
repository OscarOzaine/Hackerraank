
class Node:

	data = None
	next = None

	def __init__(self, data):
		self.data = data
		self.next = None

	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext
		

class UnorderedList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		counter = 0
		while current != None:
			counter+1
			current = current.getNext()
		return counter






# class LinkedList:

# 	data = None
# 	next = None


# 	def __init__(self, data):
# 		self.data = data

# 	def getData(self):
# 		return self.data


# 	def addItem(self, item):

# 		node = self
# 		print node.data
# 		while node.next != None:
# 			print node.data
# 			node = node.next

# 		node.data = item




mlist = UnorderedList()
mlist.add(1)
mlist.add(2)
mlist.add(3)
print mlist.size()
#while mlist.head != None:
	#print mlist.head.data
	#mlist = mlist.head
#print mlist.head
#print mlist.data
#print mlist.next.data
