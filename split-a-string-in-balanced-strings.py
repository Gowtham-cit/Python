"""
https://leetcode.com/problems/split-a-string-in-balanced-strings/submissions/
"""

#solution #Greedy Algorithm

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        c = count = 0
        
        for i in s:
            
            if i == 'R': c += 1
            else: c -= 1
            if c == 0: count += 1
        
        return count
