# Problem: https://leetcode.com/problems/edit-distance/
# Ref: https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition


class RecursiveSolution:
    def minDistance(self, word1, word2):
        """Naive recursive solution"""
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)

"""
+----+----+---+---+---+---+---+---+
|    | "" | a | b | c | d | e | f |
+----+----+---+---+---+---+---+---+
| "" | 0  | 1 | 2 | 3 | 4 | 5 | 6 |
+----+----+---+---+---+---+---+---+
| a  | 1  | 0 | 1 | 2 | 3 | 4 | 5 |
+----+----+---+---+---+---+---+---+
| z  | 2  | 1 | 1 |   |   |   |   |
+----+----+---+---+---+---+---+---+
| c  | 3  |   |   |   |   |   |   |
+----+----+---+---+---+---+---+---+
| e  | 4  |   |   |   |   |   |   |
+----+----+---+---+---+---+---+---+
| d  | 5  |   |   |   |   |   |   |
+----+----+---+---+---+---+---+---+
"""

class Solution:
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]) # checking left, top, diagonal
        return table[-1][-1]

print(Solution().minDistance("azced","abcdef"))