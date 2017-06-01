
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

	def dfs(self, s):
		visited = [False] * len(self.graph)
		queue = []
		queue.append(s)
		visited[s] = True

		while queue:

			s = queue.pop(len(queue)-1)
			print s,
			
			for i in self.graph[s]:
				if i < len(visited):
					if visited[i] == False:
						queue.append(i)
						visited[i] = True


	def dfsRecursive(self, start, end, visited=set(), path=[]):
		print start,
		if start == end:
			return path + [start]

		for i in self.graph[start]:

			if i not in visited:
				visited.add(i)
				p = self.dfsRecursive(i, end, visited, path + [i])
				if p:
					return p

		return ''



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
g.bfs(2)
print 

print 'dfs'
g.dfs(2)
print

print 'dfsRecursive'
path = g.dfsRecursive(2, 6)
print path
print 

