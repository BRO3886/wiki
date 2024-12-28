# question link: https://codeforces.com/problemset/problem/702/C
from typing import List


def possible(
    k: int,
    towers: List[int],
    cities: List[int],
    towers_len: int,
    cities_len: int,
) -> bool:
    count = 0

    i, j = 0, 0
    while i < m and j < n:
        if abs(towers[i] - cities[j]) <= k:
            count += 1
            j += 1
        else:
            i += 1

    return count >= len(cities)


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    cities = list(map(int, input().split()))
    towers = list(map(int, input().split()))

    low = 0
    high = 1e18
    ans = 1e18
    while low <= high:
        mid = (low + high) // 2
        if possible(mid, towers, cities, m, n):
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1

    print(int(ans))
