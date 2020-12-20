"""
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
"""
#solution
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence = sentence.split()
        
        for word in sentence:
            
            if searchWord == word[0:len(searchWord)]:
                
                return sentence.index(word)+1
        
        return -1
