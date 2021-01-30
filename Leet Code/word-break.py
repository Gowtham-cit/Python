"""
https://leetcode.com/problems/word-break/
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        ans = [False] * (len(s)+1)
        ans[0] = True
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                
                if ans[i] and s[i:j+1] in wordDict:
                    
                    ans[j+1] = True
        return ans[-1]
