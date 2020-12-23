"""
https://leetcode.com/problems/minimum-absolute-difference/
"""

#solution
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        
        arr.sort()
        
        
        #to find minimum absolute difference in arr
        mn = min(b-a for a, b in zip(arr, arr[1:]))
        
        #if b-a == mn then [a, b] will n=be stored in ans
        ans = [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]
        
        return ans
