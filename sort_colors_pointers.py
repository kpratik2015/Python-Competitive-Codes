# Problem: https://leetcode.com/problems/sort-colors

"""
3 points: low (0 values), mid (1 values) and high (2 values). low = mid = 0 and high = last index.

The mid pointer is used as index into the list to check the value.

if 0 is at m position, then swap m & l position and increment m & l.
else if 1 is at m position, then since its at right place, just increment m
else if 2 is at m position, then swap m & h position and decrement h position.

"""

from typing import List
class Solution:
  def sortColors(self, nums: List[int]) -> None:
      l, m, h = 0, 0, len(nums)-1
      while m <= h:
          if nums[m] == 0:
              nums[l], nums[m] = nums[m], nums[l]
              m += 1
              l += 1
          elif nums[m] == 1:
              m += 1
          else:
              nums[m], nums[h] = nums[h], nums[m]
              h -= 1

lst = [2, 0, 2, 1, 1, 0]
Solution().sortColors(lst)
print(lst)