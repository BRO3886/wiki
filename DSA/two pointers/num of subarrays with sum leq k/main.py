"""
Question - Find the number of subarrays with sum <= k, provided that `a[i] > 0`
"""

from typing import List


def find(arr: List[int], k: int) -> int:
    l = 0
    r = 0
    sum = 0
    n = len(arr)
    count = 0
    while r < n:
        sum += arr[r]
        while sum > k:
            sum -= arr[l]
            l += 1
        if sum <= k:
            count += r - l + 1
        r += 1
    return count


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(find(arr, k))
