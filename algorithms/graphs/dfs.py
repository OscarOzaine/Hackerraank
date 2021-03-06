
class SolveGraph:

	graph = None

	def __init__(self):
		self.graph = {}

	def addEdge(self, u, v):
		if u in self.graph:
			self.graph[u].append(v)
		else:
			self.graph[u] = {}

	def bfs(self, s):

		visited = [False]

		queue = []

		queue.append(s)
		visited[s] = True

		while queue:

			s = queue.pop(0)
			print s,

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


g = SolveGraph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print 'Following is Breadth First Traversal (starting from vertex 2)'

#g.bfs(2)
