"""
https://leetcode.com/problems/divide-two-integers
"""
#solution
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        ans = 0
        sign = 1
        
        if dividend < 0:
            dividend = -dividend
            sign = -sign
            
        if divisor < 0:
            divisor = -divisor
            sign = -sign
            
        while dividend >= divisor:
            val, n = divisor, 1
            while val+val <= dividend:
                val += val
                n += n
            dividend = dividend - val
            ans += n
        
        if sign == 1:
            return min(ans, 2**31-1)
        else:
            return max(-ans, -2**31)
