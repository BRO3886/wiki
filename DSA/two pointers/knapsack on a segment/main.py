"""
Question link - https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/E
"""

from typing import List


def solve(weights: List[int], costs: List[int], n: int, s: int) -> int:
    ans = float("-inf")

    l, r = 0, 0
    curr_weight, curr_cost = 0, 0

    for r in range(0, n):
        curr_weight += weights[r]
        curr_cost += costs[r]

        while l <= r and curr_weight > s:
            curr_weight -= weights[l]
            curr_cost -= costs[l]
            l += 1

        ans = max(curr_cost, ans)

    return ans


if __name__ == "__main__":
    n, s = map(int, input().split())
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    print(solve(weights, costs, n, s))
