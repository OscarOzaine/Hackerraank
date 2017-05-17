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


	def uniquePaths(self, m, n):

		matrix = [int(x) for x in xrange(m)]
		graph = {}
		for x in matrix:
			mat = [int(y) for y in xrange(n)]
			matrix[x] = mat
			
			for y in matrix[x]:
				graph[(x, y)] = {}
				graph[(x, y)] = self.getNeighbors(matrix, x, y, m, n)


		paths = self.find_all_paths(graph, (0,0), (m-1, n-1))
		
		minn = 999999999
		for i in paths:
			if len(i) < minn:
				minn = len(i)
				countmin = 0
			elif len(i) == minn:
				countmin+=1
			
		print countmin
		

		#print paths


	def find_all_paths(self, graph, start, end, path=[], countmin=0, minn=100):
		path = path + [start]
		if start == end:
			return [path, countmin]
		if not graph.has_key(start):
			return []

		paths = []
		for node in graph[start]:
			if node not in path:
				newpaths = self.find_all_paths(graph, node, end, path, countmin, minn)
				
				if len(newpaths)>0:
					print newpaths
					for newpath in newpaths[0]:
						#print newpath
						if len(newpath) < minn:
							minn = len(newpath)
							countmin = 0
						elif len(newpath) == minn:
							countmin += 1

						paths.append(newpath)
		#print countmin
		return [paths, countmin]
		






solution = Solution()

solution.uniquePaths(3, 7)