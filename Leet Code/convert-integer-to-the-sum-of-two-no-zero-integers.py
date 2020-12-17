"""
https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers

"""
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        #RunTime 24 ms #Memory 14.2 MB
        i=1
        while i<=n:
            req=n-i
            if "0" not in str(req) and "0"not in str(i):
                return [i,req]
            i=i+1
        
        

        
        """
        #solution First solved
        if n == 2 : return [1, 1]
        
        for i in range(1, n):
            for j in range(i+1, n):
                if '0' not in str(i) and '0' not in str(j):
                    if i + j == n:
                        return [i, j]
        
        
        #Runtime:1664 ms     #Memory:14.4 MB

        """
