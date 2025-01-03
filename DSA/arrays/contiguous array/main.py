"""
Question link - https://leetcode.com/problems/contiguous-array/description/
TC: O(n)
"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        rs_map = {0: 0}

        sum = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sum -= 1
            else:
                sum += 1

            if sum in rs_map:
                ans = max(ans, i - rs_map[sum] + 1)
            else:
                rs_map[sum] = i + 1

        return ans


if __name__ == "__main__":
    n = list(map(int, input().split()))
    print(Solution().findMaxLength(n))
