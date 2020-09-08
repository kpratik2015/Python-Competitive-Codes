# Problem: https://leetcode.com/problems/powx-n/

'''
+-----+---+---------+---+---------+--------------+
|     |   | x^(n/2) | * | x^(n/2) | if n is even |
+-----+---+---------+---+---------+--------------+
| x^n | = | x       | * | x^(n-1) | if n is odd  |
+-----+---+---------+---+---------+--------------+
|     |   | 1       |   |         | if n = 0     |
+-----+---+---------+---+---------+--------------+

Steps are reduced for even powers. While for odd, x * x^(n-1)
e.g. x^8 -> x^4 -> x^2 -> x^1 -> x^0
x^8 = (x*x)^4
'''

class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1) # if n is odd
        # y = self.myPow(x, n/2)
        # return y * y
        return self.myPow(x * x, n / 2) # if n is even
        
print(Solution().myPow(0.0001, 4242323213))