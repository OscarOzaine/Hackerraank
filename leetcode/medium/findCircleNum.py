class Solution(object):
	def dfs(self, M, node, seen):

		for nei, adj in enumerate(M[node]):
			print nei, adj
			if adj and nei not in seen:
				seen.add(nei)
				self.dfs(M, nei, seen)

		print
		return seen


	

	def findCircleNum(self, M):

		N = len(M)
		seen = set()

		circles = 0
		for i in xrange(N):
			#print i
			if i not in seen:
				seen = self.dfs(M, i, seen)
				circles+=1
		#print 
		return circles





solution = Solution()

circles = solution.findCircleNum([[1,1,0], [1,1,0], [0,0,1]])
#print circles
circles = solution.findCircleNum([[1,1,0], [1,1,1], [0,1,1]])
#print circles
