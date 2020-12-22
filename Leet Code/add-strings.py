"""
https://leetcode.com/problems/add-strings/
"""
#solution
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        result1 = result2 = 0
        
        for digit in num1:
            
            result1 *= 10
            
            for d in "0123456789":
                
                result1 += digit > d
        
        for digit in num:
            
            result2 *= 10
            
            for d in "0123456789":
                
                result2 += digit > d
        
        return str(result1 + result2)
