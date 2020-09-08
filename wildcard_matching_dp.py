# Problem: https://leetcode.com/problems/wildcard-matching/
# Ref: https://www.youtube.com/watch?v=3ZDZ-N0EPV0 and https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration

'''
Time complexity for 2D matrix -> O(m x n)
+----+----+---+---+---+---+
|    | "" | * | a | * | b | Pattern
+----+----+---+---+---+---+
| "" | T  | T | F | F | F |
+----+----+---+---+---+---+
| a  | F  | T | T | T | F |
+----+----+---+---+---+---+
| d  | F  | T | F | T | F |
+----+----+---+---+---+---+
| c  | F  | T | F | T | F |
+----+----+---+---+---+---+
| e  | F  | T | F | T | F |
+----+----+---+---+---+---+
| b  | F  | T | F | T | T |
+----+----+---+---+---+---+
  String
'''

class Solution:
    def isMatch(self, s, p):
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True # empty pattern matches an empty string
        for j in range(1, len(p)+1): # For a pattern like ***a against aaaba this is needed
            if p[j-1] != '*':
                break
            dp[0][j] = True  # For an empty string, a pattern of * will be True as it matches
        # Both loops skip [0][0] and pattern is matched against string so string loop is outer loop
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1] # look at diagonal value for ? or same character
                elif p[j - 1] == '*':
                    """
                    look at left or top value
                    when we're looking at left, we take * as 0 sequence of values
                    and when we look at top, we take the character as part of * as * can take anything
                    """
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] 
        return dp[-1][-1]

