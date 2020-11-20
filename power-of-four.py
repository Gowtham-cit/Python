"""
https://leetcode.com/problems/power-of-four

"""

#solution

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 0: return False
        
        if n == 1: return True
        
        if n == 4: return True
        
        if n % 4 != 0: return False
        else: return self.isPowerOfFour(int(n/4))

