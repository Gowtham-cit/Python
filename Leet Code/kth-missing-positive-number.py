class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        Array = list(range(10000)) #list to store all values
        
        
        #remove the elements in Array which is in arr also
        for i in arr:
            Array.remove(i)
        
        return Array[k]
