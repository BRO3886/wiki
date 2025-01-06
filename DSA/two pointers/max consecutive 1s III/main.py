"""
Question link  - https://leetcode.com/problems/max-consecutive-ones-iii/
TC - O(n)
"""

from typing import List

"""
    Intuition: Use a sliding window to find longest subarray that can be made all 1s
    by flipping at most k zeros.
    
    The window expands (r pointer) as long as we have used ≤ k flips.
    When we exceed k flips, we shrink window from left until we're valid again.
    
    For example: [1,1,0,0,1], k=1
    Window grows: [1] -> [1,1] -> [1,1,0](flip) -> [1,1,0,0](need 2 flips, invalid)
    Shrink left: [1,0,0] -> [0,0] -> [0]
"""


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0

        l, r = 0, 0
        n = len(nums)
        count_0 = 0
        while r < n:
            if nums[r] == 0:
                count_0 += 1

            if count_0 <= k:
                ans = max(ans, r - l + 1)

            while l <= r and count_0 > k:
                if nums[l] == 0:
                    count_0 -= 1
                l += 1

            r += 1

        return ans


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    s = Solution()
    print(s.longestOnes(nums, k))
