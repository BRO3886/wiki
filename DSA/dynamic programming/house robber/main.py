"""
Question link - https://leetcode.com/problems/house-robber/description/
TC: O()
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        self.cache = {}
        return self.rob_helper(nums, 0)

    def rob_helper(self, nums, i):
        if i >= len(nums):
            return 0

        if i in self.cache:
            return self.cache[i]

        self.cache[i] = max(
            nums[i] + self.rob_helper(nums, i + 2), self.rob_helper(nums, i + 1)
        )
        return self.cache[i]
