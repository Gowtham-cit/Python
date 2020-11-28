"""
https://leetcode.com/problems/to-lower-case/
"""
#solution
class Solution:
    def toLowerCase(self, str: str) -> str:
        s = ""
        
        for i in str:
            x = ord(i)
            if 65 <= x <= 90:
                
                s += chr(x+32)
            else:
                s += i
        return s
