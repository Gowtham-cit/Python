"""
https://leetcode.com/problems/jewels-and-stones/
"""
#solution
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
       
       
        return sum(map(stones.count, jewels))
        
        """
        c = 0
        
        for i in jewels:
            c += stones.count(i)
        return c
        """
