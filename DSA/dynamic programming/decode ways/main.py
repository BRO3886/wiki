"""
Question link - https://leetcode.com/problems/decode-ways/description/
TC: O(n)
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        self.cache = {}
        return self.solve(s, 0)

    def solve(self, s, i):
        if i > len(s):
            return 0
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0

        if i in self.cache:
            return self.cache[i]

        ways = self.solve(s, i + 1)

        if i + 1 < len(s):
            char = int(s[i : i + 2])
            if char >= 1 and char <= 26:
                ways += self.solve(s, i + 2)

        self.cache[i] = ways

        return ways
