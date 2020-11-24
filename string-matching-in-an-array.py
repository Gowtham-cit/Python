"""
https://leetcode.com/problems/string-matching-in-an-array/submissions
"""

#solution
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        copy = words.copy() #copying the list 
        ans = []
        #checking for substring
        for i in words:
            for j in copy:
                if i in j:
                    ans.append(i)
        
        sol = []
        #omitting the least(count=1)
        for i in ans:
            if ans.count(i)>=2:
                sol.append(i) 
        
        
        return list(set(sol)) #removing duplicates
