## Breadth First Search: Shortest Reach
## https://www.hackerrank.com/challenges/bfsshortreach

import sys

def build_graph(N, M):
    graph = [0]
    while (N > 0):
        graph.append([])
        N -= 1

    while (M > 0):
        (x, y) = [int(x) for x in sys.stdin.readline().split(" ")]
        graph[x].append(y)
        graph[y].append(x)
        M -= 1

    return graph

def bfs(S, graph):

    distances = {S: 0}
    queue = []
    queue.append(S)
    while queue:
        element = queue.pop(0)
        distance = distances[element] + 6
        for neighbor in graph[element]:
            if (neighbor in distances):
                continue
            distances[neighbor] = distance
            queue.append(neighbor)
    return distances


T = int(sys.stdin.readline())

for i in range(0, T):
    (N, M) = [int(x) for x in sys.stdin.readline().split(" ")]
    
    graph = build_graph(N, M)
    S = int(sys.stdin.readline())
    distances = bfs(S, graph)
    
    for i in range(1, N + 1):
        if (i == S):
            continue
        if i in distances:
            print distances[i],
        else:
            print - 1,
    print 

    T -= 1
