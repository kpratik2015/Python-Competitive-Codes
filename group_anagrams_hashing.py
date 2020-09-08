# Problem: https://leetcode.com/problems/group-anagrams/
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        buckets = {}
        for s in strs:
            bucket = ''.join(sorted(s))
            if bucket in buckets:
                buckets[bucket].append(s)
            else:
                buckets[bucket] = [s]
        return list(buckets.values())

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]