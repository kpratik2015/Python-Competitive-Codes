# Problem: https://leetcode.com/problems/permutations-ii/

# Note: digits can repeat
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(nums, path, res):
            if not nums:
                res.append(path)
                # return # backtracking
            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], res) # nums would be everything excluding current num added in path
        dfs(nums, [], res)
        return res


print(Solution().permuteUnique([3,3,0,3]))