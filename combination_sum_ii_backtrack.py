from typing import List

# Problem: https://leetcode.com/problems/combination-sum-ii/

'''
Note:
1. Each number in candidates may only be used once in the combination. (hence, i+1)
2. The solution set must not contain duplicate combinations.
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, start, remain, path, res):
            # out
            if remain == 0:
                res.append(path)
                return
            # divide
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                  continue # avoid same siblings
                if remain < candidates[i]:
                  break
                dfs(candidates, i+1, remain-candidates[i], path+[candidates[i]], res)
        res = []
        candidates = sorted(candidates)
        dfs(candidates, 0, target, [], res)
        return res