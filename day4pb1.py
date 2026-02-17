class Solution(object):
    def moveZeroes(self, nums):
        zerocount=0
        i=0
        while i<len(nums):
            if nums[i]==0:
                nums.pop(i)
                zerocount+=1
            else:
                i=i+1

        for i in range(zerocount):
                nums.append(0)