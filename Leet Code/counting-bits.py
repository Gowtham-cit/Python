"""
https://leetcode.com/problems/counting-bits/
"""
#solution
class Solution:
    def countBits(self, num: int) -> List[int]:
        
        ans = []
        for i in range(0, num+1):
            ans.append(bin(i).count('1'))
        return ans
            
