# N queen problem. 
# In NXN chess board, you have to arrange N queens such that they do not interfere each other. Following is how you define interference of queens.
# 1. Two queens cannot be on the same diagonal
# 2. Two queens cannot be in same horizontal or vertical line
# 3. Queen can jump like a knight. So, two queens cannot be at a position where they can jump two and half steps like a knight and reach the other queen.

# You should return the possible ways to arrange N queens on a chess board.

class Solution:

    nMax = 20
    #bool row[nMax], col[nMax], diag1[2*nMax], diag2[2*nMax]
    N = None
    nSolutions = 0
    queens[nMax] = None

    def __init__(self):
        for i in range(0, self.nMax):
            row[i] = col[i] = True

        for i in range(0, self.nMax):
            for j in range(0, self.nMax):
                diag1[i+j] = diag2[self.nMax+i-j] = True

    def putAQueen(k):

        if k >= self.N:
            nSolutions+=1
            print 'way #' + str(nSolutions)

            for i in range(0, self.N):
                for j in range(0, self.N):
                    if j != self.queens[i]:
                        print '+'
                    else:
                        print 'Q'
                print 

        else:

            for i in range(0, N):
                if row[i] and diag1[i + k] and diag2[self.nMax + i - k]:
                    if k == 0 or (k == 1 and abs(self.queens[k - 1] - i) != 2) or (k >= 2 and (abs(self.queens[k - 1] - i) != 2) and (abs(self.queens[k - 2] - i != 1))):
                        row[i] = False
                        diag1[i+k] = False
                        diag2[Nmax+i-k] = False
                        Queens[k] = i
                        putAQueen(k + 1)
                        row[i] = True
                        diag1[i+k] = True
                        diag2[Nmax+i-k] = True


solution = Solution()
solution.setN(14)
solution.solve()
solution.putAQueen(0)

