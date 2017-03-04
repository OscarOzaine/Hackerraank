## Route Between Nodes
## Cracking the Code Interview
## 4.1
## Given a directed graph, design an algorithm to find out wether there is a route
## between two nodes

def find_path(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path

	if not graph.has_key(start):
		return None

	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path)
			if newpath: return newpath

	return None

N = int(raw_input().strip())

graph = {}
for i in range(65, 65 + N):
	graph[chr(i)] = raw_input().strip().split(' ')

a, b = raw_input().strip().split(' ')

path = find_path(graph, a, b)
if path:
	print 'There is a path between ' + str(a) + ' and ' + str(b)
	print path 
else:
	print 'No path found'
