
class Node:
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
			counter+=1
			current = current.getNext()
		return counter

	def search(self, item):

		current = self.head

		while current != None:
			if current.data == item:
				return True
			current = current.getNext()

		return False

	def remove(self, item):

		current = self.head

		while current != None:
			if current.data == item:
				temp = current.getNext()
				if temp:
					current.data = temp.data
					current.next = temp.next
				else:
					current.data = None
					current.next = None
				return True

			current = current.getNext()

		return False


mlist = UnorderedList()
mlist.add(1)
mlist.add(2)
mlist.add(3)
mlist.add(4)
mlist.add(5)
mlist.add(6)


print mlist.search(2)
print mlist.search(4)

mlist.remove(2)
mlist.remove(4)

print mlist.search(2)
print mlist.search(4)

print mlist.size()

