"""
https://leetcode.com/problems/string-without-aaa-or-bbb
"""
#solution
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        if a == b:
            return "ab" * a
        
        if a > b:
            H, L = a, b
            x, y = "ab"
        else: # B<A
            H, L = b, a
            x, y = "ba"
        
        bins    = L+1
        doubles = H - bins
        x2      = x*2
        res     = [x2] * doubles + [x] * (bins-doubles)
        
        return y.join(res)
