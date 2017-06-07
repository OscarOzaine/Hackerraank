from collections import deque

def append_if(grid, queue, x, y):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        if grid[x][y] == 1:
            queue.append((x, y))


def mark_neighbors(grid, row, col):
    queue = deque()

    queue.append((row, col))

    while queue:
        x, y = queue.pop()
        grid[x][y] = '2'

        append_if(grid, queue, x - 1, y)
        append_if(grid, queue, x, y - 1)
        append_if(grid, queue, x + 1, y)
        append_if(grid, queue, x, y + 1)


def countClouds(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return 0

    row_length = len(grid)
    col_length = len(grid[0])

    island_counter = 0
    for row in range(row_length):
        for col in range(col_length):
            if grid[row][col] == 1:
                # found an island
                island_counter += 1

                mark_neighbors(grid, row, col)

    return island_counter

skyMap = [
    [0, 1, 1, 0, 1], 
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1]
]

#skyMap = [["1","1","1","1","1","1","1"]]

print countClouds(skyMap)
'''

def getNeighbors(graph, i, j, visited):

    neighbors = []

    if len(graph) -1> i and (i+1, j) not in visited:
        neighbors.append((i+1, j))

    if i > 0 and (i-1, j) not in visited:
        neighbors.append((i-1, j))

    if len(graph[0])-1 > j and (i, j+1) not in visited:
        neighbors.append((i, j+1))

    if j > 0 and (i, j-1) not in visited:
        neighbors.append((i, j-1))

    return neighbors


def dfs(graph, start, visited=set()):
    #print 'a',start
    queue = [start]
    #print queue
    while queue:

        start = queue.pop(0)
        #print 'start', start
        i = start[0]
        j = start[1]

        if start not in visited:

            visited.add(start)
            neighbors = getNeighbors(graph, i, j, visited)
            for n in neighbors:
                #print 
                if n not in visited and int(graph[n[0]][n[1]]) == 1:
                    #print 't=', n, n[0], n[1]
                    queue.append(n)
        

    #print visited
    return visited

def countClouds(skyMap):
    
    visited = set()
    x = 0
    y = 0
    counter = 0
    #print skyMap
    
    for i in range(0, len(skyMap)):

        for j in range(0, len(skyMap[i])):
            #print (i, j), visited
            
            if (i, j) not in visited and int(skyMap[i][j]) == 1:
                vis = dfs(skyMap, (i, j), visited)
                visited = vis.union(visited)
                #print (i, j)
                #print visited
                #for v in vis:
                    #if v not in visited:
                        #visited.append(v)
                        #print (v)
                #print visited
                counter += 1
            
            
            #print skyMap[i][j],
            
        #print 
    
    return counter


skyMap = [
    [0, 1, 1, 0, 1], 
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1]
]

#skyMap = [["1","1","1","1","1","1","1"]]

print countClouds(skyMap)

'''