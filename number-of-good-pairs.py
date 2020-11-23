"""
https://leetcode.com/problems/number-of-good-pairs/
"""
#solution
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        dct = {}
        ans = 0
        
        for i in nums:
            
            if i not  in dct:
                dct[i] = 1
            
            else:
                ans += dct[i]
                dct[i] += 1
        
        return ans
