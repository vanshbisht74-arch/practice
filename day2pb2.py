class Solution(object):
    def isPalindrome(self, x):
        rev=0
        original=x
        while x !=0:
            temp=x%10
            rev=rev*10+temp
            x=x//10

        return rev
        if rev==original:
            return True
        else:
            return False

