def roadsBuilding(cities, roads):
    if cities == 1:
        return []
    
    result = []
    for i in range(0, cities):
        for j in range(i+1, cities):
            if i != j:
                if [i, j] not in roads and [j,i] not in roads:
                    result.append([i,j])
                    roads.append([j,i])
                    roads.append([i,j])
                
    
    return result
    
