"""
https://leetcode.com/problems/number-of-1-bits/
"""

#solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        return bin(n).count('1')
            
        
