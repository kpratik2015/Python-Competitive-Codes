# Problem: https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums):
        if len(nums) <= 1: return 0
        l, r = 0, nums[0] # l pointer starts at 0 and r is distance jumped
        jumps = 1 # 1 jump by default as r is initiated to first element's value
        while r < len(nums) - 1:
            jumps += 1 # taking jump already in account as it can exceed the len(nums) in next loop and lower number jump is allowed
            print(f"figure out next best distance between {l} and {r}")
            jumping = [i + nums[i] for i in range(l, r + 1)]
            print(f"jumpings {jumping}")
            # nxt = max(i + nums[i] for i in range(l, r + 1)) # OPTIMIZED
            nxt = max(jumping) # next distance will be the max. obtainable adding variations of current jump value and element at jumped distance
            l, r = r, nxt
            print(f"[l] {l}, [r] {r}")
        return jumps

print(Solution().jump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))