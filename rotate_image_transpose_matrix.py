# Problem: https://leetcode.com/problems/rotate-image/
# Ref: https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

# Rotate matrix by 90 degrees (clockwise)

'''
+---+---+---+     +---+---+---+
| 1 | 2 | 3 |     | 7 | 4 | 1 |
+---+---+---+     +---+---+---+
| 4 | 5 | 6 |  => | 8 | 5 | 2 |
+---+---+---+     +---+---+---+
| 7 | 8 | 9 |     | 9 | 6 | 3 |
+---+---+---+     +---+---+---+
'''

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        print(f"Reversed Matrix: {matrix}")
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)
print(matrix)