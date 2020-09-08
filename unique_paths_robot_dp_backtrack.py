# Problem: https://leetcode.com/problems/unique-paths/

"""
A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?
"""

# Backtracking solution timesout
class BacktrackSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.paths = 0
        target = (m-1, n-1)
        def dfs(path, target):
            x, y = path
            if target[0] == x and target[1] == y:
                self.paths += 1
                return
            for move in ["down", "right"]:
                if move == "down":
                    cur_x, cur_y = path
                    if cur_y + 1 < n:
                        dfs((cur_x, cur_y+1), target)
                else:
                    cur_x, cur_y = path
                    if cur_x + 1 < m:
                        dfs((cur_x+1, cur_y), target)
        dfs((0,0), target)     
        return self.paths

"""
The numbers in grid represent number of ways to reach at that spot
+---+---+---+     +---+---+---+
| 1 | 1 | 1 |     | 1 | 1 | 1 |
+---+---+---+     +---+---+---+
| 1 | 1 | 1 | ->  | 1 | 2 | 3 |
+---+---+---+     +---+---+---+
| 1 | 1 | 1 |     | 1 | 3 | 6 |
+---+---+---+     +---+---+---+
"""

# DP Solution
# O (m*n) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

print(Solution().uniquePaths(3, 3))

# O(n) space 
def uniquePaths(m, n):
    if not m or not n:
        return 0
    cur = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            cur[j] += cur[j-1]
    return cur[-1]