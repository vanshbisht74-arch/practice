#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        rs=""
        for ch in s:
            rs=ch+rs
        
        return rs
            