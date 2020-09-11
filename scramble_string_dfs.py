# Problem: https://leetcode.com/problems/scramble-string/

"""
Input: s1 = "abcde", s2 = "caebd"
Output: false
"""

class Solution:
    # DFS with memorization
    def __init__(self):
        self.dic = {}
    
    def isScramble(self, s1: str, s2: str) -> bool:
        print(f"[s1] {s1} v/s [s2] {s2}")
        if (s1, s2) in self.dic:
            return self.dic[(s1, s2)]
        if len(s1) != len(s2) or sorted(s1) != sorted(s2): # prunning
            self.dic[(s1, s2)] = False
            return False
        if s1 == s2:
            self.dic[(s1, s2)] = True
            return True
        for i in range(1, len(s1)):
            # 0..i and i..-1 or 0..i v/s reversed and i..-1 v/s reversed
            print(f"{s1[:i]} == {s2[:i]} and {s1[i:]} == {s2[i:]} OR {s1[:i]} == {s2[-i:]} and {s1[i:]} == {s2[:-i]}")
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
            (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        self.dic[(s1, s2)] = False
        return False


print(Solution().isScramble("great", "rgeat"))