"""
Question link - https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
TC: O(n)
"""

"""
Intuition: To make a string monotone increasing (all 0s before all 1s), 
we try each position as a potential split point between 0s and 1s. 
For each position i:
- All elements before i must become 0 (so we count 1s to flip)
- All elements after i must become 1 (so we count 0s to flip)
The answer is minimum of (ones_before_i + zeros_after_i) across all positions.
We use prefix sum to efficiently count ones before any position.
Time: O(n), Space: O(n)
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        ones_b4 = [0] * (n + 1)
        for i in range(n):
            ones_b4[i + 1] = ones_b4[i] + (1 if s[i] == "1" else 0)
        minflips = float("inf")
        for i in range(n + 1):
            f = ones_b4[i]
            z = (n - i) - (ones_b4[n] - ones_b4[i])
            minflips = min(minflips, z + f)

        return minflips
