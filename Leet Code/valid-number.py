"""
https://leetcode.com/problems/valid-number/
"""
#solution
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False
