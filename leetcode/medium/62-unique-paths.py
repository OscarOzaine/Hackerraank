# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach 
#  the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

# Input
# 1
# 2

#X X X
#X X X
#X X X


class Solution(object):

	def uniquePaths(self, m, n):
		aux = [[1 for x in range(n)] for x in range(m)]
		print aux
		for i in range(1, m):
			for j in range(1, n):
				aux[i][j] = aux[i][j-1] + aux[i-1][j]

		print 
		print aux
		return aux[-1][-1]
	

	countermin = 0
	min_value = 999999

	def getNeighbors(self, matrix, posx, posy, maxx, maxy):
		neighbors = []
		if posx < maxx:
			neighbors.append((posx+1, posy))

		if posx > 0:
			neighbors.append((posx-1, posy))

		if posy < maxy:
			neighbors.append((posx, posy+1))

		if posy > 0:
			neighbors.append((posx, posy-1))

		return neighbors


	def uniquePaths2(self, m, n):

		matrix = [int(x) for x in xrange(m)]
		graph = {}
		for x in matrix:
			mat = [int(y) for y in xrange(n)]
			matrix[x] = mat
			
			for y in matrix[x]:
				graph[(x, y)] = {}
				graph[(x, y)] = self.getNeighbors(matrix, x, y, m, n)


		paths = self.find_all_paths(graph, (0,0), (m-1, n-1))
		
		return self.countermin


	def find_all_paths(self, graph, start, end, path=[]):
		path = path + [start]
		if start == end:

			if len(path) < self.min_value:
				self.min_value = len(path)
				self.countermin = 0
			elif len(path) == self.min_value:
				self.countermin += 1

			return [path]
		if not graph.has_key(start):
			return []
		paths = []
		for node in graph[start]:
			if node not in path:
				if len(path) < self.min_value:
					#print path
					newpaths = self.find_all_paths(graph, node, end, path)

					for newpath in newpaths:
						#print newpath
						paths.append(newpath)
				else:
					return [path]

		return paths
		





solution = Solution()

print solution.uniquePaths(7, 13)