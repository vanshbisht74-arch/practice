class Solution:
    def factorial(self,x):
    fact=1  
    for i in range(1,x+1):
        fact=fact*i
    return fact


f1=Solution()
print(f1.factorial(3))