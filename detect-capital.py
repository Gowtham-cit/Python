"""
https://leetcode.com/problems/detect-capital
"""
#sollution
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        #All letters in this word are capitals
        if all(map(lambda x : x.isupper(), word)) : return True
        
        #All letters in this word are not capitals
        if all(map(lambda x : x.islower(), word)) : return True
    
        #Only the first letter in this word is capital
        if word[0].isupper() and all(map(lambda x : x.islower(), word[1:])): return True
        
        #Otherwise
        return False
