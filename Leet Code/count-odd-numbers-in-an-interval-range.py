"""
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Formula : count = (largestOdd - smallestOdd)/ 2 + 1
        
        """
        #to find smallest odd
        #if low is even :: example low = 2 then low = 2+1
        
        if low % 2 == 0:
            low = low + 1
        #else low is odd :: then no change (low=low)
        
        
        #to find largest odd
        #if high is even :: example  = 4 then high = 4 - 1
        if high % 2 == 0:
            high = high - 1
        #else high is odd :: then no change(high=high)
        
        
        #formunla
        ans = (high - low) / 2 + 1
        
        
        return int(ans)
