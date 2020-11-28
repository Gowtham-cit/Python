"""
https://leetcode.com/problems/split-a-string-in-balanced-strings/submissions/
"""

#Two solutions #Greedy Algorithm

class Solution1:
    def balancedStringSplit(self, s: str) -> int:
        
        c = count = 0
        
        for i in s:
            
            if i == 'R': c += 1
            else: c -= 1
            if c == 0: count += 1
        
        return count
    
class Solution2:
    def balancedStringSplit(self, s: str) -> int:
        
        R_count = L_count = 0
        Balanced_count = 0
        
        for i in s:
            
            if i == 'R':
                R_count += 1
            else:
                L_count += 1
            
            if R_count == L_count:
                Balanced_count += 1
                R_count = L_count = 0
        
        return Balanced_count
                
                
        
