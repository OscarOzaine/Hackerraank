import sys

def matrixElementsSum(matrix):
	length = len(matrix[0])
	n = len(matrix)
	counter = 0
	for i in range(0, n):
		for j in range(0, length):
			if matrix[i][j] == 0:
				for x in range(i, n):
					matrix[x][j] = 0
				
	for i in range(0, n):
		for j in range(0, length):
			counter += matrix[i][j]
	
	return counter
	
			
	
	

n = int(raw_input().strip())

matrix = []
for i in range(0, n):
	row = map(int, raw_input().strip().split(' '))
	matrix.append(row)

print matrixElementsSum(matrix)

