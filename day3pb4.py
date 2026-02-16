class Solution(object):
    # one pointer method best to start swapping left elemts with right nad stoping when left become greter than right.
    def reverseString(self, s):
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1