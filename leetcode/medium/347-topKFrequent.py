'''
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 < k < number of unique elements.
Your algorithms time complexity must be better than O(n log n), where n is the array's size.

'''


import operator

class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		hashmap = {}
		for n in nums:
			if n in hashmap:
				hashmap[n] += 1
			else:
				hashmap[n] = 1

		kValues = sorted(hashmap.items(), key=operator.itemgetter(1), reverse=True)
		#print kValues
		if k < kValues:
			nums = []
			i = 0
			for kValue in kValues:
				#print i
				if i >= k:
					break
				i+=1
				nums.append(kValue[0])
				#print i[0]
			return nums
		return -1
		#print hashmap, nums, k


s = Solution()

nums = [1,1,1,2,2,3]
k = 2

print s.topKFrequent(nums, k)

