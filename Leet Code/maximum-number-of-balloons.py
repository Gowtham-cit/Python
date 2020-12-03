"""
https://leetcode.com/problems/maximum-number-of-balloons/
"""

#solution

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        balloon = {"b":0, "a":0, "l":0, "o":0, "n":0}
        
        for i in text:
            
            if i in balloon:
                balloon[i] += 1
                
        balloon['l'] //= 2
        balloon['o'] //= 2
        ans = min(balloon.values())
        
        return ans
