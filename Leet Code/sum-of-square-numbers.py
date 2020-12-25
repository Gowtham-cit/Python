"""
https://leetcode.com/problems/sum-of-square-numbers
"""
#solution
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        sq = set()
        count = int(c ** 0.5)
        
        for i in range(count+1):
            sq.add(i**2)
        
        for i in sq:
            if c - i in sq:
                return True
