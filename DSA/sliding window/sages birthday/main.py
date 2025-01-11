"""
Question link - https://codeforces.com/problemset/problem/1419/D2
"""

import math
from typing import List, Tuple


def solve(prices: List[int], n: int) -> Tuple[int, List[int]]:
    if n <= 2:
        return (0, prices)

    reordered = [0] * n
    prices.sort()

    j = 0
    for i in range(1, n, 2):
        reordered[i] = prices[j]
        j += 1
    for i in range(0, n, 2):
        reordered[i] = prices[j]
        j += 1

    count = sum(
        [
            (
                1
                if reordered[i] < reordered[i - 1] and reordered[i] < reordered[i + 1]
                else 0
            )
            for i in range(1, n - 1, 2)
        ]
    )

    return count, reordered


if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))

    count, reordered = solve(prices, n)
    print(count)
    print(*reordered)
