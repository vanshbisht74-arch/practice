class Solution(object):
    def isAnagram(self, s, t):
        sorts="".join(sorted(s))
        sortt="".join(sorted(t))

        return sorts==sortt

        