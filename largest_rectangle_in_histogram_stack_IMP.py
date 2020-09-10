# Problem: https://leetcode.com/problems/largest-rectangle-in-histogram/

# CHECK ALSO maximal_rectangle_stack

class Solution:
    def largestRectangleArea(self, height):
        height.append(0) # appending 0 at the end of height list for our convenience
        stack = [-1] # initialize stack with -1 so it picks up 0 height from height array
        ans = 0 # ans stores the max area so far
        for i in range(len(height)):
            print(f"i {i}")
            while height[i] < height[stack[-1]]: # When we are at a height that breaks the ascending height in stack
                h = height[stack.pop()]  # get height of index at top of stack and simultaneously remove that index from stack
                print(f"h {h} from index {i-1} and top index now {stack[-1]}")
                w = i - stack[-1] - 1  # width is lower height index (stack[-1]) subtracted from index to the left of i which will be the index that was at the top of stack
                ans = max(ans, h * w)
                print(f"Rectangle: {stack[-1]}<->{i-1} [A]: {ans} and stack {stack}")
            stack.append(i) # store index onto stack as it has higher height than the current index at top of stack
        height.pop() # cleaning up the 0 we put
        return ans

print(Solution().largestRectangleArea([1, 2, 3, 2, 1, 0, 2, 1, 1, 0]))
                                      #0  1  2  3  4  5  6  7  8  9
"""
Rectangles considered:
1<->2 i.e.  heights 2 <-> 3 [A]: 3 stack [-1, 0, 1]
1<->3 i.e.  heights 2 <-> 2 [A]: 4 and stack [-1, 0, 1]
0<->3 i.e.  heights 1 <-> 2 [A]: 6 and stack [-1, 0]
0<->4 i.e.  heights 1 <-> 1 [A]: 6 and stack [-1, 0]
-1<->4 i.e. heights 0 <-> 1 [A]: 6 and stack [-1]
5<->6 i.e.  heights 0 <-> 2 [A]: 6 and stack [-1, 5]
7<->8 i.e.  heights 1 <-> 1 [A]: 6 and stack [-1, 5, 7]
5<->8 i.e.  heights 0 <-> 1 [A]: 6 and stack [-1, 5]
"""