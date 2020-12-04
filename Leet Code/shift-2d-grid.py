"""
https://leetcode.com/problems/shift-2d-grid/
"""
#solution

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        Row_len = len(grid)
        Col_len = len(grid[0])
        
        Temp = [0] * Row_len * Col_len
        
        k = k % (Row_len * Col_len)
        
        for i in range(Row_len):
            for j in range(Col_len):
                
                Temp[i * Col_len + j] = grid[i][j]
        
        Temp = Temp[-k:] + Temp[:-k]
        
        for i in range(Row_len):
            for j in range(Col_len):
                
                grid[i][j] = Temp[i * Col_len + j] 
        
        
        return grid
