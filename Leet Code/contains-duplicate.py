"""
https://leetcode.com/problems/contains-duplicate/
"""

#solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = list(set(nums))
        
        return len(num) == len(nums)
