# Problem: https://leetcode.com/problems/set-matrix-zeroes/

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_affected = set()
        col_affected = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_affected.add(i)
                    col_affected.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row_affected or j in col_affected:
                    matrix[i][j] = 0
        return matrix

print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))