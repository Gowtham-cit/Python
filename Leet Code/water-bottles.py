"""
https://leetcode.com/problems/water-bottles/
"""
#solution
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        x, y = numBottles, numExchange
        
        return int(x + (x-1)/(y-1))
