"""
https://leetcode.com/problems/complement-of-base-10-integer/
"""

#solution
class Solution1:
    def bitwiseComplement(self, N: int) -> int:
        
        ans = ""
        for i in str(bin(N))[2:]:
            
            if i == '1':
                ans += "0"
                
            if i == '0':
                ans += "1"
                
        return int(ans, 2)

class Solution2:
  def bitwiseComplement(self, N: int) -> int:
        X = 1
        while N > X: X = X * 2 + 1
        return N ^ X

