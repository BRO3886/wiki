"""
Question - https://leetcode.com/problems/max-consecutive-ones/
TC: O(n)
"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        max_ans = 0
        for num in nums:
            if num == 1:
                ans += 1

            if num == 0:
                ans = 0

            if max_ans < ans:
                max_ans = ans

        return max_ans
