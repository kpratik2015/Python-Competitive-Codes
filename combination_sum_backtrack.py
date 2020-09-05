# Problem: https://leetcode.com/problems/combination-sum/
from typing import List
'''
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def backtrack(remain, comb, start):
            if remain == 0: # done condition
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0: # failed path condition 
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()
        
        backtrack(target, [], 0)
        
        return results

print(Solution().combinationSum([2,3,6,7], 7))