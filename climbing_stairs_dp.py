# Problem: https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        dp = [1,2,3] + [0] * (n-3)
        for i in range(3, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

print(Solution().climbStairs(45))