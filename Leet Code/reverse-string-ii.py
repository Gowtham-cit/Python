"""
https://leetcode.com/problems/reverse-string-ii/

"""

#solution
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k > len(s):
            return s[::-1]
        s = list(s)
        for i in range(0, len(s), k * 2):
            s[i:i + k] = s[i:i + k][::-1]
        return ''.join(s)
        
