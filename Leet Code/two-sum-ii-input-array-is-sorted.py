"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
"""
#solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]]+1,i+1]
            else:
                required[nums[i]]=i
