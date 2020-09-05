# Problem: https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        mapper = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        itr = 0
        for i in range(len(num1)-1,-1,-1):
            if itr == 0:
                n1 += mapper[num1[i]]
            else:
                n1 += mapper[num1[i]] * (10**itr)
            itr += 1
        itr = 0
        for i in range(len(num2)-1,-1,-1):
            if itr == 0:
                n2 += mapper[num2[i]]
            else:
                n2 += mapper[num2[i]] * (10**itr)
            itr += 1
        return str(n1 * n2)
        
print(Solution().multiply("123", "456"))