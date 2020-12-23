"""
https://leetcode.com/problems/check-if-n-and-its-double-exist/
"""
#solution
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        if arr.count(0) > 1:
            return True
        else:
            
            if 0 in arr:
                arr.remove(0)
            
            for i in range(len(arr)):
                
                if arr[i] * 2 in arr :
                    
                    return True
