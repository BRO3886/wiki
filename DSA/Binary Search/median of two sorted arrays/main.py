# Question Link - https://leetcode.com/problems/median-of-two-sorted-arrays/
import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)

        l, r = 0, n

        while l <= r:
            mid1 = (l + r) // 2
            mid2 = (n + m + 1) // 2 - mid1

            l1 = -math.inf if mid1 == 0 else nums1[mid1 - 1]
            l2 = -math.inf if mid2 == 0 else nums2[mid2 - 1]
            r1 = math.inf if mid1 == n else nums1[mid1]
            r2 = math.inf if mid2 == m else nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                ans = max(l1, l2)
                if (n + m) % 2 == 0:
                    return (ans + min(r1, r2)) / 2
                else:
                    return ans
            if l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1
