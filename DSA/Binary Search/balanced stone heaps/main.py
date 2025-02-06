"""
Question link - https://codeforces.com/problemset/problem/1623/C
Title - Balanced Stone Heaps
TC - 
Time s, Memory MB
"""

from typing import List


def check(arr: List[int], mid: int, n: int) -> bool:
    b = [0] * n
    for i in range(n - 1, 1, -1):
        if arr[i] + b[i] - mid < 0:
            return False

        d = min(arr[i], arr[i] + b[i] - mid) // 3
        b[i - 1] += d
        b[i - 2] += 2 * d

    return arr[0] + b[0] >= mid and arr[1] + b[1] >= mid


def solve(arr: List[int], n: int) -> int:
    l = min(arr)
    h = max(arr)
    ans = l
    while l <= h:
        mid = l + (h - l) // 2
        if check(arr, mid, n):
            ans = mid
            l = mid + 1
        else:
            h = mid - 1

    return ans


testing = False

if __name__ == "__main__":
    if testing:
        n = 4
        arr = [1, 2, 10, 100]
        print(solve(arr, n))
    else:
        t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solve(arr, n))
