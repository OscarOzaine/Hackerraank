class Solution(object):
    def rotate(self, nums, k):
    	#copy array
        a = nums[:]
        for i in range(0, len(nums)):
        	print i, k, len(nums)
        	print len(nums)/k
        	
        	print (i+k) % len(nums)
        	print 
        	a[(i+k) % len(nums)] = nums[i]

        for i in range(0, len(nums)):
        	nums[i] = a[i]

solution = Solution()
nums = [1,2,3,4,5,6,7]
solution.rotate(nums, 3)
print nums



