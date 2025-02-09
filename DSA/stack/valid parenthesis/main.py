"""
Question link - https://leetcode.com/problems/valid-parentheses/description/
Title - Valid Parentheses
TC - O(n)
Time s, Memory MB
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        for ch in s:
            if ch in "{([":
                stack.append(ch)
            elif ch in "})]":
                if not stack or stack.pop() != pairs[ch]:  # not while!
                    return False

        return len(stack) == 0
