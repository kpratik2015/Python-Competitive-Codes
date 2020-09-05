# Compute how much water it is able to trap after raining
# Problem: https://leetcode.com/problems/trapping-rain-water/ (img: https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
from typing import List

# Note: 1. for l pointer, advancement means increment and for r pointer, advancement means decrement 2. l_max and r_max are compared

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        volume = 0
        l, r = 0, len(height) - 1 # pointers initialized l=0, r=n-1
        l_max, r_max = height[l], height[r] # max for both side initialized to first and last element, respectively
        while l < r: # pointer while
            l_max, r_max = max(height[l], l_max), max(height[r], r_max) # refresh max in each iteration
            if l_max <= r_max: # for the lesser max, operation is done against current bar and respective pointer is advanced
                volume += l_max - height[l]
                l += 1
            else:
                volume += r_max - height[r]
                r -= 1
        return volume

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))