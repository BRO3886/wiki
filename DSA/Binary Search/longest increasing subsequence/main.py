"""
Question link - https://leetcode.com/problems/longest-increasing-subsequence/
TC: O(nlogn)
"""

from typing import List

"""
Question link - https://leetcode.com/problems/longest-increasing-subsequence/
TC: O(nlogn)
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        temp = [nums[0]]
        for i in range(1, n):
            if temp[-1] < nums[i]:
                temp.append(nums[i])
            else:
                pos = self.find_pos(temp, nums[i])
                temp[pos] = nums[i]

        return len(temp)

    def find_pos(self, temp: List[int], num: int) -> int:
        low = 0
        high = len(temp)
        while low <= high:
            mid = (low + high) // 2
            if temp[mid] >= num:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
