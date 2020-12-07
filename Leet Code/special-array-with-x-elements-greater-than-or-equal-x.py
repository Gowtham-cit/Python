""""
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

"""
#solution
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        if nums[0] >= n:
            return n
        
        for i in range(1, n):
            
            greater = n - i
            
            if nums[i] >= greater and nums[i-1] <greater:
                return greater
            
        return -1
            
