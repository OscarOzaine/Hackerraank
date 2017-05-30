
class Node:
	data = None
	root = None
	left = None
	right = None

	def __init__(self, data):
		self.data = data

def longestConsecutive(root, consecutive=1, longest=1):

	if root == None:
		return longest

	lng1 = 0
	lng2 = 0

	if root.left:
		
		if root.left.data + 1 == root.data:
			consecutive += 1

			if consecutive>longest:
				longest = consecutive

			lng1 = longestConsecutive(root.left, consecutive, longest)
		else:
			lng1 = longestConsecutive(root.left, 1, longest)


	if root.right:

		if root.right.data - 1 == root.data:

			consecutive += 1

			if consecutive > longest:
				longest = consecutive

			lng2 = longestConsecutive(root.right, consecutive, longest)
		else:
			lng2 = longestConsecutive(root.right, 1, longest)



	mm = lng2

	if lng1 > mm:

		mm=lng1

	if mm > longest:
		return mm

	return longest


root = Node(6)

root.right = Node(9)
root.right.left = Node(7)
root.right.left.left = Node(6)
root.right.left.left.left = Node(5)
root.right.left.left.left.left = Node(4)

root.right.right = Node(10)

root.right.right.right = Node(11)
root.right.right.right.right = Node(12)
root.right.right.right.right.right = Node(13)

num = longestConsecutive(root)

print 'longest consecutive sequence = ' + str(num)
