class Solution(object):
    def findCircleNum(self, M):
        circles = {}
        for i in range(len(M)):
            for j in range(len(M)):

            	if i != j:
            		if i not in circles:
            			circles[i] = [j]
            		else:
            			circles[i].append(j)

            		if j not in circles:
            			circles[j] = [i]
            		else:
            			circles[j].append(i)

        for i in circles:
        	print set(circles[i])
        print circles
                

solution = Solution()

solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
        
        