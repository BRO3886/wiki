"""
Question - Given an array of N elements find out the length of the longest subarray with number of distinct elements <= k
"""

from typing import List


def find(arr: List[int], k: int) -> int:
    ans = 0
    l, r = 0, 0
    n = len(arr)
    sum = 0
    freq = {}
    while r < n:
        if freq.get(arr[r]) == None:
            freq[arr[r]] = 1
        else:
            freq[arr[r]] += 1

        while l <= r and len(freq) > k:
            sum -= arr[l]
            freq[arr[l]] -= 1
            if freq[arr[l]] <= 0:
                del freq[arr[l]]
            l += 1

        sum += arr[r]

        if len(freq) <= k:
            ans = max(ans, r - l + 1)

        r += 1

    return ans


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    print(find(arr, k))
