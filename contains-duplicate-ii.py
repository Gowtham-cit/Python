"""
https://leetcode.com/problems/contains-duplicate-ii/
"""

#solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dct = {}
        
        for i in range(len(nums)):
            
            if nums[i] in dct and abs(i-dct[nums[i]]) <= k:
                
                return True
            dct[nums[i]] = i
        return False
