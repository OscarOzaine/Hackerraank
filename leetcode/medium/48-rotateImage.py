'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5,  1,  9, 11],
  [ 2,  4,  8, 10],
  [13,  3,  6,  7],
  [15, 14, 12, 16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15, 13,  2,  5],
  [14,  3,  4,  1],
  [12,  6,  8,  9],
  [16,  7, 10, 11]
]

'''

class Solution(object):
    combinations = []
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.combinations = []
        for x in range(0, len(matrix) - 1):
            for i in range(1, len(matrix)):
                matrix = self.firstSwap(matrix, x, i)


        for x in range(0, len(matrix)):
            matrix[x] = list(reversed(matrix[x]))

    def firstSwap(self, matrix, x, i):
        if (x, i) not in self.combinations and (i, x) not in self.combinations:
            self.combinations.append((x, i))
            temp = matrix[x][i] 
            matrix[x][i] = matrix[i][x]
            matrix[i][x] = temp

        return matrix


matrix = [
  [5, 1, 9, 11],
  [2, 4, 8, 10],
  [13, 3, 6, 7],
  [15, 14, 12, 16]
]

s = Solution()
s.rotate(matrix)

#print matrix
