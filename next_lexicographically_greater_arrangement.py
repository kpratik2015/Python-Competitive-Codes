'''
1. From end, find the first decreasing element (say k)
2. From the index of k, find number to the right which is just greater than k (say j)
3. Swap both (k & j)
4. Reverse elements next to index of i.
'''
from typing import List
def nextPermutation(nums: List[int]) -> None:
  """
  Do not return anything, modify nums in-place instead.
  """
  i = j = len(nums)-1
  while i > 0 and nums[i-1] >= nums[i]: # move i to left till next is greater than current
    i -= 1
  if i == 0:   # nums are in descending order
    nums.reverse()
    return 
  k = i - 1    # k points to element which breaks ascending trend
  while nums[j] <= nums[k]: # decrement j until nums[j] is smaller or equal to element at k
    j -= 1
  nums[k], nums[j] = nums[j], nums[k]  
  l, r = k+1, len(nums)-1  # reverse the second part
  while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l += 1; r -= 1

nums = [9, 5, 4, 3, 1]
nextPermutation(nums)
print(nums)

# Animation: https://leetcode.com/media/original_images/31_Next_Permutation.gif