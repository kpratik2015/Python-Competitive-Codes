# Problem: https://leetcode.com/problems/search-a-2d-matrix/

"""
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
"""
from typing import List
class MySolution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        elif not matrix[0]:
            return False
        elif target <= matrix[0][-1]:
            return target in matrix[0]
        elif target > matrix[0][-1]:
            matrix.pop(0)
            return self.searchMatrix(matrix, target)

class BinarySearchSolution:
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        while low <= high:
            mid = (low + high) // 2 # low + (high - low) // 2
            num = matrix[mid // cols][mid % cols] # This is a property caused by the mid indices filling the rows then the columns ("horizontally" then "vertically"). We can't do matrix[mid//rows][mid%rows]
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

print(BinarySearchSolution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11))