"""
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent
"""
#solution
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        if "".join(word1) == "".join(word2):
            return True
        return False
