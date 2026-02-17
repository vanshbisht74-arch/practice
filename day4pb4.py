class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n

        while k>0:
            last=nums.pop()
            nums.insert(0,last)
            k=k-1