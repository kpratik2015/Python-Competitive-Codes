# Problem: https://leetcode.com/problems/minimum-path-sum/
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1] # first column's path value is initialized by adding to previous path
            
        for j in range(1, len(grid)):
            grid[j][0] += grid[j-1][0] # similarly for first row
        
        for i in range(1,len(grid)):
            for j in range(1, len(grid[i])):
                if grid[i-1][j] <= grid[i][j-1]:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += grid[i][j-1]
        return grid[-1][-1]

print(Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))

# 7 i.e. 1 -> 3 -> 1 -> 1 -> 1