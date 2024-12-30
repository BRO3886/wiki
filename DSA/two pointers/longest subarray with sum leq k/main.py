"""
Question - Given an array of N positive elements, find out the length of the longest subarray with sum <= k.
"""

from typing import List


def find(arr: List[int], k: int) -> int:
    ans = 0
    l, r = 0, 0
    n = len(arr)
    sum = 0
    while r < n:
        while l <= r and sum > k:
            sum -= arr[l]
            l += 1
        sum += arr[r]
        if sum <= k:
            ans = max(ans, r - l + 1)
        r += 1

    return ans

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(find(arr, k))
