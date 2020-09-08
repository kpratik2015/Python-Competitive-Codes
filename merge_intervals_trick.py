# Problem: https://leetcode.com/problems/merge-intervals/

"""
Note: sorting is important.
Sorting ensures we only have to update previous interval's end as start will be always lower.
"""

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        for interval in sorted(intervals, key=lambda i: i[0]):
            # if interval's start is less than or equal to previous interval's end i.e. it lies within bound of previous interval
            # e.g. interval = [2,6] and out[-1] = [1,3]
            # we update previous interval's end to the max one
            if out and interval[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], interval[1]) 
            else:
                out += interval, # out = out + [interval] # comma is important in currently used form
        return out

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))