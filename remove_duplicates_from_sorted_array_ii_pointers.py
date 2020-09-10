# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
"""

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            print(f"n {n} with i {i} and i-2 element {nums[i-2]}")
            if i < 2 or n > nums[i-2]: # in the start, nums[-2] i.e. last 2nd element
                nums[i] = n
                i += 1
        return i

print(Solution().removeDuplicates([1,1,1,1,2,2,2,2]))