"""
https://leetcode.com/problems/valid-mountain-array


Let us start from the left of our arr and go to the right until it is possible, 
that is until our data is increasing. Also we start from the end and go to the left until our data is decreasing. 
If we met somwhere in the middle in point, which is neither 0 nor n-1, it means that we found our mountain, in other case array is not mountain.
"""

#solution

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)
        beg, end = 0, n - 1

        while beg != n-1 and arr[beg + 1] > arr[beg]: beg += 1
            
        while end != 0 and arr[end - 1] > arr[end]: end -= 1
            
        return beg == end and end != n-1 and beg != 0
