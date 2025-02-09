"""
Question link - https://leetcode.com/problems/next-greater-element-i/
Title - Next Greater Element I
TC - O(N)
Time s, Memory MB
"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            res[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])

        return [res[num] for num in nums1]
