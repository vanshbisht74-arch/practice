class Solution:
    def sumOfDigits(self, n):
        sum=0
        while n>0:
            temp=n%10
            sum=sum+temp
            n=n//10
            
        
        return sum