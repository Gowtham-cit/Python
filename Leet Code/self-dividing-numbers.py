"""
https://leetcode.com/problems/self-dividing-numbers/
"""
#solution
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        answer = []
        
        for i in range(left, right+1):
            
            if self.isSelf(i):
                
                answer.append(i)
        return answer
        
        
        
    def isSelf(self, num):

        temp = num

        while temp:
            div = temp % 10
            if not div or num % div != 0:
                return False
            temp //= 10
        return True
