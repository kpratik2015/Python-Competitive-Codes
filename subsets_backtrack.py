# Problem: https://leetcode.com/problems/subsets/

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [nums]
        max_len = len(nums)
        
        def dfs(nums, path, res, max_len):
            if not max_len:
                return
            res.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]], res, max_len-1)
                
        dfs(nums, [], res, max_len)
        return res

print(Solution().subsets([1,2,3]))