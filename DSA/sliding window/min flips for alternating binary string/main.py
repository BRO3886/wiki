"""
Question link - https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/
TC - O(n)
"""

import math

"""
Intuition:
- Double string (s+s) lets us try all rotations using sliding window
- Only 2 possible alternating patterns: '1010..' or '0101..'
- Track flips needed for both patterns in each window
- Sliding window removes old chars and adds new ones, simulating rotation
- Answer is minimum flips across all possible rotations
"""


class Solution:
    def minFlips(self, s: str) -> int:
        s2 = s + s
        n = len(s)
        t1 = ["1" if i % 2 == 0 else "0" for i in range(2 * n)]
        t2 = ["0" if i % 2 == 0 else "1" for i in range(2 * n)]
        m = math.inf
        f1 = f2 = 0
        for i in range(2 * n):
            if s2[i] != t1[i]:
                f1 += 1
            if s2[i] != t2[i]:
                f2 += 1
            if i >= n:
                if s2[i - n] != t1[i - n]:
                    f1 -= 1
                if s2[i - n] != t2[i - n]:
                    f2 -= 1

            if i >= n - 1:
                m = min(m, f1, f2)
        return m
