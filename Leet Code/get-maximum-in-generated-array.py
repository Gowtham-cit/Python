"""
https://leetcode.com/problems/get-maximum-in-generated-array/

"""

#solution

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n == 0:
            return 0
        ans =[0] * (n*2)
        ans[1] = 1
        
        for i in range(n + 1):
            if i % 2 == 0: ans[i] = ans[i//2]
            else: ans[i] = ans[i//2] + ans[i//2 + 1]
        return max(ans)
