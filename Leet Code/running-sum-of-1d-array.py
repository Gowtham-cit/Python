"""
https://leetcode.com/problems/running-sum-of-1d-array/
"""
#solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for i in range(len(nums)):
        
            ans.append(sum(nums[0:i+1]))
        
        return ans
