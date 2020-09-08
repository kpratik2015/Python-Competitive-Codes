# Problem:
# Ref: https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)

# Get the kth permutation of n digits

"""
say n = 4, you have {1, 2, 3, 4}

If you were to list out all the permutations you have

1 + (permutations of 2, 3, 4)
2 + (permutations of 1, 3, 4)
3 + (permutations of 1, 2, 4)
4 + (permutations of 1, 2, 3)

We know how to calculate the number of permutations of n numbers... n! So each of those with permutations of 3 numbers means there are 6 possible permutations. Meaning there would be a total of 24 permutations in this particular one. So if you were to look for the (k = 14) 14th permutation, it would be in the

3 + (permutations of 1, 2, 4) subset.

{1, 2, 3, 4}, k/(n-1)! = 13/(4-1)! = 13/3! = 13/6 = 2. The array {1, 2, 3, 4} has a value of 3 at index 2. So the first number is a 3
"""

import math
class Solution:
    def getPermutation(self, n, k):
        numbers = [str(i) for i in range(1, n+1)]
        permutation = ''
        k -= 1 # as index starts at 0
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))  # k/(n-1)!
            permutation += numbers[index]
            # remove handled number
            numbers.remove(numbers[index]) # Adds O(n) to complexity which makes it O(n^2)
            print(f"index [{index}], k [{k}], numbers [{numbers}]")

        return permutation

print(Solution().getPermutation(4, 14))