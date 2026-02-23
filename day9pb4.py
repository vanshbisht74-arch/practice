class Solution:
    def firstElementKTime(self, arr, k):
        for i in range(len(arr)):
            if arr.count(arr[i]) >= k:
                return arr[i]
        return -1