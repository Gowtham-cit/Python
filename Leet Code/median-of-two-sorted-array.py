"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
#solution
#user input
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        lst = nums1 + nums2
        lst.sort()
        x = int(len(lst)/2)
        
        
        if len(lst) % 2 == 0: #if length of the lst is even then if part
            lst = lst[x] + lst[x -1]
            return lst/2
        else: #if the length of the lst is odd then else part
            return lst[x]
