# Problem: https://leetcode.com/problems/maximum-subarray/
# Ref: https://www.youtube.com/watch?v=2MmGzdiKR9Y

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        # curSum stores the best contiguous array sum till i-1 point
        for num in nums[1:]:
            curSum = max(num, curSum + num) # either the number itself is current best sum or current number + best sum till prev. point is better
            maxSum = max(maxSum, curSum) # maxSum is updated
        return maxSum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))