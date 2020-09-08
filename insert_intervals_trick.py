# Problem: https://leetcode.com/problems/insert-interval/

# Note: intervals assumed sorted by their start coordinate

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = newInterval
        for index, i in enumerate(intervals):
            # current end is less than newInterval's start then append current and continue
            if n[0] > i[1]: # n comes later than current interval. Determined from current interval's end
                res.append(i)
            # n's end is less than current's start i.e. new interval fits before current
            elif n[1] < i[0]:
                res.append(n)
                return res+intervals[index:]  # can return earlier as new interval is fitted
            else:  # overlap case, only change new interval values
                # either n's start or end lie in between or on current interval
                n[0] = min(n[0], i[0])
                n[1] = max(n[1], i[1])
        res.append(n) # no fit found for new interval so must be at the end
        return res

print(Solution().insert([[1,3],[6,9]],[2,5])) # [[1,5],[6,9]]