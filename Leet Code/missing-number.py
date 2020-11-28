"""
https://leetcode.com/problems/missing-number/
"""

#solution


class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n+1):
            if i not in nums:
                return i
       
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        
        return sum(range(0, len(nums)+1)) - sum(nums)
