# Problem: https://leetcode.com/problems/sqrtx/

"""
    - since 1 <= x <= x^2 for all x > 0
    - we are going to search for a number that which sqaure is just right a bit larger than x

    e.g. 8
    1 2 3 4 5 6 7 8
    ^             ^

    1 2 3 4 5 6 7 8
    ^     ^

    1 2 3 4 5 6 7 8
        ^   ^

    1 2 3 4 5 6 7 8
        ^
    3^2 = 9 is larger than 8, therefore answer should be 3-1=2

    Time    O(logn)
    Space   O(1)
"""
class BinarySearchSolution():
    def mySqrt(self, x):
        if x == x*x:
            return x
        left = 1
        right = x
        while left < right:
            mid = (left + right)/2
            if x >= mid*mid:
                left = mid + 1
            else:
                right = mid
        return left-1

class Solution:
    def mySqrt(self, x: int) -> int:
        r = x + 1  # avoid dividing 0
        while r*r > x:
                r = int(r - (r*r - x)/(2*r))  # newton's method
        return r
                


print(Solution().mySqrt(8))