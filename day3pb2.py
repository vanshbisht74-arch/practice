class Solution(object):
    def tribonacci(self, n):
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        a=0
        b=1
        c=1
        while n>2:

            d=a+b+c
            a=b
            b=c
            c=d
            n=n-1

        return c