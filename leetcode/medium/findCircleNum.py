class Solution(object):
	def removeKey(self, d, key):
		r = dict(d)
		print r
		del r[key]

		print r
		return r

	def findCircleNum(self, M):
		circles = {}
		for i in range(len(M)):
			for j in range(len(M)):

				if i != j:
					if M[i][j] == 1:

						if i not in circles:
							circles[i] = [j]
						elif j not in circles[i]:
							circles[i].append(j)

						if j not in circles:
							circles[j] = [i]
						elif i not in circles[j]:
							circles[j].append(i)

		#circles = range(M)
		res = len(M)
		print res
		print 

		circs = circles.copy()#[:]

		for i in circles:
			#print circs
			#print circs.keys()
			#print circs.values()
			#print circles[i]
			#print circs.keys()
			#print 
			if i in circs.values():
				print 'yep'
				print i, circles[i]
				circs = self.removeKey(circs, i)
				

		print circs
                

solution = Solution()

#solution.findCircleNum([[1,1,0], [1,1,0], [0,0,1]])

solution.findCircleNum([[1,1,0], [1,1,1], [0,1,1]])
