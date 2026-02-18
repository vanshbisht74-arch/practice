class Solution(object):
    def removeDuplicates(self, nums):
    
        if len(nums)==0:
            return 0

        k=1

        for i in range(1,len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1


        return k    

        
        