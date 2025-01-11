"""
Question link - https://codeforces.com/problemset/problem/1623/C
Title - Balanced Stone Heaps
TC - 
Time 1s, Memory 256 MB
"""

from typing import List


def check(d: int, heaps: List[int], n: int) -> bool:
    hc = heaps.copy()

    for i in range(n - 1, 2, -1):
        if hc[i] <= d:
            return False

        c1 = max(0, d - hc[i - 1])
        c2 = max(0, d - hc[i - 2])

        have = hc[i] - d

        if c1 + c2 > 0:
            mind = max((c1 + 0.5) // 1, c2 // 2)
            if 3 * mind <= have:
                hc[i] -= 3 * mind
                hc[i - 1] += mind
                hc[i - 2] += 2 * mind
            else:
                return False

    return hc[0] >= d and hc[1] >= d


def search(heaps: List[int], n: int) -> int:
    low = 0
    high = 1e10
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid, heaps, n):
            low = mid + 1
            ans = max(ans, mid)
        else:
            high = mid - 1

    return int(ans)


if __name__ == "__main__":
    tc = int(input())
    for i in range(tc):
        n = int(input())
        heaps = list(map(int, input().split()))
        print(search(heaps, n))
