'''
rowCount = 0
colCount = 0
arrA = []

def printAll(arrA, currentRow, currentColumn, path):

	if currentRow == rowCount - 1:
		for i in range(currentColumn, colCount):
			path += '-' + arrA[currentRow][i]

		print path
		return

	if currentColumn == colCount - 1:
		for i in range(currentRow, rowCount - 1):
			path += '-' + arrA[i][currentColumn]

		print path


	path = path + '-' + str(arrA[currentRow][currentColumn])
	printAll(currentRow + 1, currentColumn, path)
	printAll(currentRow, currentColumn + 1, path)


array = [[1, 2, 3], [4, 5, 6]]
printAll(array, 0, 0, '')

'''

def printAllPathsUtil(mat, i, j, m, n, path, pi):
	if (i == m - 1):
		for k in range(j, n):
			#print mat, i, j, k, path
			path[pi + k - j] = (mat[0][0] + i*n) + k

		for l in range(0, pi + n - j):
			#print path, l
			print str(path[l]),

		print 

		return

	if (j == n - 1):
		for k in range(i, m):
			#print mat, i, j, k, path
			path[pi + k - i] = (mat[0][0]+k*n)+ j

		for l in range(0, pi + m - i):
			#print path, l
			print str(path[l]),# + ' ', path

		print 
		return

	#print mat, i, j, pi
	path[pi] = mat[i][j]#((mat + i*n) + j)

	printAllPathsUtil(mat, i+1, j, m, n, path, pi + 1)
	printAllPathsUtil(mat, i, j+1, m, n, path, pi + 1)

def printAllPaths(mat, m, n):
	path = {}
	printAllPathsUtil(mat, 0, 0, m, n, path, 0)

matrix = [
	[1, 2, 3, 4], 
	[5, 6, 7, 8], 
	[9, 10, 11, 12], 
	[13, 14, 15, 16]
]

printAllPaths(matrix, 4, 4)

