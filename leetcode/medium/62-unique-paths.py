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
			neighbors.append([posx+1, posy])

		if posx > 0:
			neighbors.append([posx-1, posy])

		if posy < maxy:
			neighbors.append([posx, posy+1])

		if posy > 0:
			neighbors.append([posx, posy-1])

		#neighbors = [int(x) for x in neighbors: if
		return neighbors


	def uniquePaths(self, m, n):

		matrix = [int(x) for x in xrange(m)]
		graph = {}
		for x in matrix:
			mat = [int(y) for y in xrange(n)]
			matrix[x] = mat
			
			#print matrix[x]
			graph[x] = mat
			graph[x] = {}
			for y in matrix[x]:
				graph[x][y] = {}
				graph[x][y] = self.getNeighbors(matrix, x, y, m, n)


		queue = [x for x in graph[0][0]]

		print self.dijkstra(graph, [0,0], [m-1, n-1])


	def dijkstra(self, graph, src, dest, visited=[], distances={}, predecessors={}):
		""" calculates a shortest path tree routed in src
		"""    
		# a few sanity checks
		if src not in graph:
			raise TypeError('The root of the shortest path tree cannot be found')
		if dest not in graph:
			raise TypeError('The target of the shortest path cannot be found')    
			# ending condition
		if src == dest:
			# We build the shortest path and display it
			path=[]
			pred=dest
			while pred != None:
				path.append(pred)
				pred=predecessors.get(pred,None)
			print('shortest path: '+str(path)+" cost="+str(distances[dest])) 
		else:
			# if it is the initial  run, initializes the cost
			if not visited: 
				distances[src]=0
			# visit the neighbors
			for neighbor in graph[src] :
				if neighbor not in visited:
					new_distance = distances[src] + graph[src][neighbor]
					if new_distance < distances.get(neighbor,float('inf')):
						distances[neighbor] = new_distance
						predecessors[neighbor] = src
			# mark as visited
			visited.append(src)
			# now that all neighbors have been visited: recurse                         
			# select the non visited node with lowest distance 'x'
			# run Dijskstra with src='x'
			unvisited={}
			for k in graph:
				if k not in visited:
					unvisited[k] = distances.get(k,float('inf'))        
			x=min(unvisited, key=unvisited.get)

			self.dijkstra(graph, x, dest, visited, distances, predecessors)


	def bfs(self, graph, start, end):

		if start == end:
			return 
		print end


		#queue = [graph[0][0]]
		#while queue:
		#	last = queue.pop(0)
		#	print last

		




solution = Solution()

solution.uniquePaths(3, 7)