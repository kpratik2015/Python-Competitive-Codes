# Problem: https://leetcode.com/problems/spiral-matrix/

'''
Sovling it by spinning/transposing and popping

I/P:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
O/P:
[1,2,3,6,9,8,7,4,5]

Note: zip() combines one element from each list at a time as a tuple
'''

class Solution:
    def spiralOrder(self, matrix):
        result = []
        while matrix:
            result.extend(matrix[0])
            matrix.pop(0)
            print(f"From matrix {matrix} to zipping matrix: {list(zip(*matrix))}")
            matrix = list(zip(*matrix))[::-1]
        return result

print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

'''
From matrix [[4, 5, 6], [7, 8, 9]] to zipping matrix: [(4, 7), (5, 8), (6, 9)]
From matrix [(5, 8), (4, 7)] to zipping matrix: [(5, 4), (8, 7)]
From matrix [(5, 4)] to zipping matrix: [(5,), (4,)]
From matrix [(5,)] to zipping matrix: [(5,)]
[1, 2, 3, 6, 9, 8, 7, 4, 5]
'''