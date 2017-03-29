import sys

 
	
	

n = int(raw_input().strip())

matrix = []
for i in range(0, n):
	row = map(int, raw_input().strip().split(' '))
	matrix.append(row)

print matrixElementsSum(matrix)

