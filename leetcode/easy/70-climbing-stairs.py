class Solution(object):
    count = 0
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.count = 0
        self.helper(n, 0, {})

        return self.count
        
    def helper(self, n, start, memo = {}):
    	if start > n:
    		return 0

    	if start == n:
    		#self.count += 1
    		return 1

    	if start in memo and memo[start] > 0:
    		return memo[start]

    	memo[start] = self.helper(n, start + 1, memo) + self.helper(n, start + 2, memo)

    	return memo[start]




s = Solution()

n = 35

print s.climbStairs(n)

