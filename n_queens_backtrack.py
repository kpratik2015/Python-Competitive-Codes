# Problem: https://leetcode.com/problems/n-queens/
# Solution: https://leetcode.com/problems/n-queens/discuss/19971/Python-recursive-dfs-solution-with-comments.

"""
Here,
nums -> array of position of queens placed at each row
index/start -> which row/level queen is being evaluated to be placed
comb/path -> placement of Q along with preceeding and suceeding "."
backtrack condition -> index reached len(nums) i.e. filled all positions
"""

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res
 
    # nums is a one-dimension array, like [1, 3, 0, 2] means
    # first queen is placed in column 1, second queen is placed
    # in column 3, etc.
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return  # backtracking
        for i in range(len(nums)):
            nums[index] = i # marking i as potential placement of Q at level `index`
            if self.valid(nums, index):  # pruning
                tmp = "."*len(nums)
                self.dfs(nums, index+1, path+[tmp[:i]+"Q"+tmp[i+1:]], res)

    # check whether nth queen can be placed in that column
    def valid(self, nums, n):
        for i in range(n):  # checking position with all previous Q
            """
            Two fail conditions:
            1. On same column as any previous queen
            2. distance between columns [abs(nums[n] - nums[i])] is same as distance between rows (n-i)
            abs(y2-y1/x2-x1) == 1 i.e. rise/run = slope (m) of 45 degree, where m is tan 45 
            A 45 degree slope is diagonal
            """
            if abs(nums[i]-nums[n]) == n-i or nums[i] == nums[n]:
                return False
        return True

print(Solution().solveNQueens(4))