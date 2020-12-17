"""
https://leetcode.com/problems/excel-sheet-column-number/
"""
#solution

class Solution:
    def titleToNumber(self, s: str) -> int:
        
        r, count = len(s)-1, 0
        
        c = 0
        
        
        #To get  A -> 1 B -> 2 C -> 3 ....... Z -> 26
        #example D -> 4
        #To get 4 
        #ord('D') - ord('A') + 1 = 4
        #Here ord() will return ascii value of char
        def getNumber(char):
            return ord(char) - ord('A') + 1 
        
        
        #Iteration for all char in s
        for char in s:
            c += pow(26, r) * getNumber(char)
            r -= 1
        return c
