class Solution(object):
    def findNonMinOrMax(self, nums):
        if len(nums)<3:
            return -1
       
        min1=min(nums)
        max1=max(nums)
        for num in nums:
            if min1!=num and max1!=num:
                return num