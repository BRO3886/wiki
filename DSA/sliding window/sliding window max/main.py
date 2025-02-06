"""
Question link - https://leetcode.com/problems/sliding-window-maximum/description/
Title - Sliding Window Maximum
TC - O(n)
Time s, Memory MB
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        ans = []
        for i in range(n):
            curr = nums[i]
            while q and q[-1] < curr:
                q.pop()
            q.append(curr)

            if i >= k and q[0] == nums[i - k]:
                q.popleft()

            if i >= k - 1:
                ans.append(q[0])

        return ans


if __name__ == "__main__":
    s = Solution()
    nums = list(map(int, input().split()))
    k = int(input())
    ans = s.maxSlidingWindow(nums, k)
    print(*ans)
