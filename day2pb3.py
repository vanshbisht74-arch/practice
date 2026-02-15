class Solution(object):
    def isHappy(self, n):
        original=n
        sum=0
        seen=[]
        while n!=1:
            if n in seen:
                return False

                seen.append(n)
            
            while n>0:
               temp=n%10
               sum=sum+temp**2
               n=n//10



            if sum==original:
             return True