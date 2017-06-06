

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


def dfs(graph, start, visited=[]):
    #print 'a',start
    
    queue = [start]

    while queue:

        start = queue.pop(0)
        #print 'start', start
        i = start[0]
        j = start[1]
        visited.append(start)
        neighbors = getNeighbors(graph, i, j, visited)
        for n in neighbors:
            #print 
            if n not in visited and int(graph[n[0]][n[1]]) == 1:
                #print 't=', n, n[0], n[1]
                queue.append(n)
    

    #print visited
    return visited
def union(self, *objects):
    """Find the sets containing the objects and merge them all."""
    roots = [self[x] for x in objects]
    heaviest = max([(self.weights[r],r) for r in roots])[1]
    for r in roots:
        if r != heaviest:
            self.weights[heaviest] += self.weights[r]
            self.parents[r] = heaviest

def countClouds(skyMap):
    refs = [[0, 0], [-1, 0], [0, -1], [1, 0], [0, 1]]
    for i in range(len(skyMap)):
        for j in range(len(skyMap[i])):
            print i, j
            for dy, dx in refs:
                is_neighbour_valid = 0 <= (i + dy) < len(skyMap) and 0 <= (j + dx) < len(skyMap[i])
                if not is_neighbour_valid:
                    continue

                current_cell, neighbour_cell = skyMap[i][j] == '1', skyMap[i + dy][j + dx] == '1'
                if current_cell and is_neighbour_valid:
                    ds.union((i, j), (i + dy, j + dx))
    
    visited = []
    x = 0
    y = 0
    counter = 0
    #print skyMap
    
    for i in range(0, len(skyMap)):

        for j in range(0, len(skyMap[i])):
            #print (i, j), visited
            
            if (i, j) not in visited and int(skyMap[i][j]) == 1:
                vis = dfs(skyMap, (i, j), visited)
                visited += vis
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


class UnionFind:
    """Union-find data structure.

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root
        
    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest


def countClouds(unionFind, skyMap):
    refs = [[0, 0], [-1, 0], [0, -1], [1, 0], [0, 1]]
    for i in range(len(skyMap)):
        for j in range(len(skyMap[i])):
            
            for dy, dx in refs:
                is_neighbour_valid = 0 <= (i + dy) < len(skyMap) and 0 <= (j + dx) < len(skyMap[i])
                if not is_neighbour_valid:
                    continue

                current_cell, neighbour_cell = int(skyMap[i][j]) == 1, int(skyMap[i + dy][j + dx]) == 1
                
                if current_cell and is_neighbour_valid:
                    unionFind.union((i, j), (i + dy, j + dx))

    return len(set(unionFind.parents.values()))



skyMap = [
    [0, 1, 1, 0, 1], 
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1]
]

#skyMap = [["1","1","1","1","1","1","1"]]
unionFind = UnionFind()
print countClouds(unionFind, skyMap)


