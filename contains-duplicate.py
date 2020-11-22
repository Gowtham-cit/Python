"""
https://leetcode.com/problems/contains-duplicate/
"""

#solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = list(set(nums))
        
        if len(num) == len(nums):
            return False
        return True
