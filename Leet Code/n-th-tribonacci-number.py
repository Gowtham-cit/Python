"""
https://leetcode.com/problems/n-th-tribonacci-number/
"""

#solution
class Solution:
    def tribonacci(self, n: int) -> int:
        
        lst = [0] * (n + 1)
        
        lst[:3] = [0, 1, 1]
        
        for i in range(3, n+1):
            
            lst[i] = sum(lst[i-3:i])
            
        
        return lst[n]
