
class SolveGraph:

	graph = None

	def __init__(self):
		self.graph = {}

	def addEdge(self, u, v):
		if u in self.graph:
			self.graph[u].append(v)
		else:
			self.graph[u] = [v]

	def bfs(self, start):
		visited = [False] * (len(self.graph))
		queue = []
		queue.append(start)
		visited[start] = True

		while queue:

			s = queue.pop(0)
			print s,

			for i in self.graph[s]:
				if i < len(visited):
					if visited[i] == False:
						queue.append(i)
						visited[i] = True


	def dfsRecursive(self, start, end, visited=set(), path=[]):
		#print start,
		visited.add(start)
		if start == end:
			return path + [start]

		for i in self.graph[start]:

			if i not in visited:
				
				p = self.dfsRecursive(i, end, visited, path + [start])
				if p:
					return p

		return ''

	def dfsRecursiveAllPaths(self, start, end):


		stack = [(start, [start])]

		while stack:
			(vertex, path) = stack.pop()
			for i in self.graph[vertex] - set(path):
				if i == goal:
					yield path + [i]
				else:
					stack.append((i, path + [i]))

	def dfs_paths(self, start, goal, path=None):
		if path is None:
			path = [start]
		if start == goal:
			yield path
		for next in self.graph[start] - set(path):
			yield self.dfs_paths(next, goal, path + [next])

			



g = SolveGraph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(2, 4)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.addEdge(6, 6)

print g.graph
print 'bfs'
g.bfs(0)
print 

print 'dfsRecursive'
path = g.dfsRecursive(0, 4)
print path
print 

print 'dfsRecursiveAllPaths'
paths = g.dfsRecursiveAllPaths(0, 4)
print path
print 

print 'dfs_paths'
paths = g.dfs_paths(3, 4)
print path
print 

