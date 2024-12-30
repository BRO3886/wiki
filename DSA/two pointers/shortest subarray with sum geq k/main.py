"""
Question - Given an array of n components find the length of the shortest subarray with sum >= k.
"""

import math
from typing import List


def find(arr: List[int], k: int) -> int:
    ans = math.inf
    l = 0
    r = 0
    n = len(arr)
    sum = 0
    while r < n:
        sum += arr[r]
        while l <= r and sum >= k:
            ans = min(ans, r - l + 1)
            sum -= arr[l]
            l += 1
        r += 1
    return ans


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(find(arr, k))
