# Problem: https://leetcode.com/problems/spiral-matrix-ii/submissions/
# Ref: https://leetcode.com/problems/spiral-matrix-ii/discuss/22443/9-lines-python-solution

"""
Spiral Matrix stores values as per coordinates, per count like: (0,0) (0,1) (0,2) (1,2) (2,2) ...
"""
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for i in range(n)] for j in range(n)]
        coord = [[(i,j) for j in range(n)] for i in range(n)]
        count = 1
        while coord:
            for x, y in coord.pop(0):
                print(f"Putting {count} at ({x},{y})")
                result[x][y] = count
                count += 1
            print(f"Transposing coord {coord}")
            coord = list(zip(*coord))[::-1]

        return result

print(Solution().generateMatrix(3))

"""
Putting 1 at (0,0)
Putting 2 at (0,1)
Putting 3 at (0,2)
Transposing coord [[(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)]]
Putting 4 at (1,2)
Putting 5 at (2,2)
Transposing coord [((1, 1), (2, 1)), ((1, 0), (2, 0))]
Putting 6 at (2,1)
Putting 7 at (2,0)
Transposing coord [((1, 1), (1, 0))]
Putting 8 at (1,0)
Transposing coord [((1, 1),)]
Putting 9 at (1,1)
Transposing coord []
[[1, 2, 3], [8, 9, 4], [7, 6, 5]]
"""