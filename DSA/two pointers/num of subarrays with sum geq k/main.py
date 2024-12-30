"""
Question - Count the number of subarrays with sum >=k given that all elements are positive.
"""

from typing import List


def find(arr: List[int], k: int) -> int:
    l = 0
    r = 0
    n = len(arr)
    sum = 0
    count = 0
    while r < n:
        sum += arr[r]
        while l <= r and sum >= k:
            count += n - r
            sum -= arr[l]
            l += 1
        r += 1
    return count


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())
    print(find(arr, k))
