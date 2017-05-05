
class Solution(object):
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        summ = 0
        i = 0
        while i < len(nums):
            summ += min(nums[i], nums[i+1])
            i += 2
        
        return summ


        