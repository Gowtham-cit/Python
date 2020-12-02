"""
https://leetcode.com/problems/distribute-candies/
"""

#solution
#detailed-solution
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        CT = len(set(candyType)) #number of Candy types
        n = int(len(candyType)/2) #maximum number Alice can eat
        
        
        #only one type of candy is available
        if CT == 1: 
            return 1
        #number-of-Candy-types == maximum-number-Alice-can-eat
        elif CT == n:
            return n
        
        #number-of-Candy-types < maximum-number-Alice-can-eat
        elif CT < n:
            return CT
        
        #number-of-Candy-types > maximum-number-Alice-can-eat
        else:
            return n

#one-line-solution
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        return min(len(candyType)//2, len(set(candyType)))
