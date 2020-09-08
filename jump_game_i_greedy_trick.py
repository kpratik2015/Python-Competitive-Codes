# Problem: https://leetcode.com/problems/jump-game/
# Ref: https://leetcode.com/problems/jump-game/discuss/20907/1-6-lines-O(n)-time-O(1)-space

'''
This is a very Philosophical problem: even if you have the smallest jump every index (every day), you will reach the last index (destination) no matter what (need no algorithm to figure out). But once you have a zero in the way, you may have troubles.
'''

def canJump(nums):
    farthest_index_possible = 0
    for i, n in enumerate(nums):
        # last farthest jump should be greater than current index in order to go ahead.
        if i > farthest_index_possible: 
            return False
        farthest_index_possible = max(farthest_index_possible, i+n)
    return True

# Fails as it reaches i = 3 and farthest_index_possible is 2
print(canJump([2,0,0,2]))