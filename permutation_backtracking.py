# Problem: https://leetcode.com/problems/permutations/

# Note: nums will only contain unique digits for this solution to work

from typing import List
class Solution:
    def permute(self, nums):
        res = []
        def dfs(nums, path, res):
            if not nums:
                res.append(path)
                # return # backtracking
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], res) # nums would be everything excluding current num added in path
        dfs(nums, [], res)
        return res

class MySolution: # Our approach but slower
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        def dfs(nums, path):
            if len(nums) == 2:
                res.append(path + nums)
                res.append(path + nums[::-1])
            
            for i in range(len(nums)):
                dfs([num for num in nums if num != nums[i]], path + [nums[i]])
        dfs(nums, [])
        # print(f"res {res}")
        return res

print(Solution().permute([1, 2, 3]))