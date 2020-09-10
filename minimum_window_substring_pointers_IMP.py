# Problem: https://leetcode.com/problems/minimum-window-substring/

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

First we get window of ADOBEC, start = 0 and end = 5. Then we move pointer to D so as to make A missing and find next A.
Now we get window of CODEBA, start = 5 and end = 10. Then we move pointer to O so as to make C missing and find next C.
Now we get window of EBANC, start = 7 and end = 11. Then we move pointer to B so to make B missing.

COUNTERS:
1. ({'A': 0, 'B': 0, 'C': 0, 'D': -1, 'O': -1, 'E': -1}) => make A += 1
2. ({'A': 0, 'C': 0, 'B': -1, 'D': -2, 'O': -2, 'E': -2}). Till we find A in DOBECODEBA, we got to B -1. So we reach C as the starting point with need of B going to 0 i.e. ({'A': 0, 'B': 0, 'C': 0, 'D': -1, 'O': -1, 'E': -1})
3. ({'A': 0, 'B': 0, 'C': 0, 'D': -1, 'O': -1, 'E': -1, 'N': -1}). Now we find first non-negative need in ODEBANC which is first at B
"""
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)            #hash table to store char frequency
        missing = len(t)                         #total number of chars we care
        start, end = 0, 0
        i = 0
        print(f"need {need}")
        for j, char in enumerate(s, 1):          #index j from 1
            print(f"Currently at char {char} and its need is {need[char]} with missing {missing}")
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:                     #match all chars
                print(f"missing == 0 with need {need} starting from {i}")
                while i < j and need[s[i]] < 0:  #remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                print(f"need of {s[i]} was non-negative and need {need}")
                need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
                missing += 1                     #we missed this first char, so add missing by 1
                if end == 0 or j-i < end-start:  #update window
                    start, end = i, j
                i += 1                           #update i to start+1 for next window
        return s[start:end]

print(Solution().minWindow("ADOBECODEBANC", "ABC"))