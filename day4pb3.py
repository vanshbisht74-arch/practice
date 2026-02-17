class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        countones=0
        maxcountones=0
        for i in range(len(nums)):
            if nums[i]==1:
                countones=countones+1
                if countones>maxcountones:
                    maxcountones=countones
            else:
                countones=0
        
        return maxcountones
