'''''''''''''''''''''
Brute foce, n^2
'''''''''''''''''''''
def leftUp(matrix, i, j):
    while i >= 0 and i <= len(matrix) - 1 and j >= 0 and j <= len(matrix) - 1:
        matrix[i][j] = 1
        i-=1
        j-=1
        
    return matrix

def leftDown(matrix, i, j):
    while i >= 0 and i <= len(matrix) - 1 and j >= 0 and j <= len(matrix) - 1:
        matrix[i][j] = 1
        i+=1
        j-=1
        
    return matrix

def rightUp(matrix, i, j):
    while i >= 0 and i <= len(matrix) - 1 and j >= 0 and j <= len(matrix) - 1:
        matrix[i][j] = 1
        i-=1
        j+=1
        
    return matrix
    
def rightDown(matrix, i, j):
    while i >= 0 and i <= len(matrix) - 1 and j >= 0 and j <= len(matrix) - 1:
        matrix[i][j] = 1
        i+=1
        j+=1
        
    return matrix
    
def squaresUnderQueenAttack(n, queens, queries):
    matrix = [[0] * n for i in range(n)]
    size = n - 1
    for q in queens:
        x1 = q[0] - 1
        x2 = q[1] - 1
        
        matrix = leftUp(matrix, q[0], q[1])
        matrix = leftDown(matrix, q[0], q[1])
        matrix = rightUp(matrix, q[0], q[1])
        matrix = rightDown(matrix, q[0], q[1])
        
            
        for i in range(0, n):
            matrix[i][int(q[1])] = 1
            matrix[int(q[0])][i] = 1
            
    
    result = []
    for q in queries:
        if matrix[q[0]][q[1]] == 1:
            result.append(True)
        else:
            result.append(False)
    
    return result


'''''''''''''''''''''
n*Log(n)
'''''''''''''''''''''
def squaresUnderQueenAttack(n, queens, queries):
    
    row = set()
    col = set()
    diagonal1 = set()
    diagonal2 = set()
    
    res = []
    
    for i, j in queens:
        row.add(i)
        col.add(j)
        diagonal1.add(j - i)
        diagonal2.add(j + i)
        
    for i, j in queries:
        if i in row or j in col or j-i in diagonal1 or j+i in diagonal2:
            res.append(True)
        else:
            res.append(False)
            
    return res

