"""
https://leetcode.com/problems/is-subsequence
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        #if S and t are same 
        if s == t: return 1
        
        s_pos = 0
        t_pos = 0
        
        test_str = ""
        
        while s_pos < len(s) and t_pos < len(t):
            
            if s[s_pos] == t[t_pos]:
                
                test_str += s[s_pos]
                
                s_pos += 1
                t_pos += 1
            else:
                t_pos += 1
        return test_str == s
