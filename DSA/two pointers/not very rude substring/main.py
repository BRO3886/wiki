"""
Question link - https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/G
"""

from typing import List


def min_rude(t: List[str], n: int, c: int) -> int:
    count_a, count_b = 0, 0
    l, r = 0, 0
    ans = 0
    curr_rudeness = 0
    for r in range(n):
        count_a += 1 if t[r] == "a" else 0
        count_b += 1 if t[r] == "b" else 0
        curr_rudeness += count_a if t[r] == "b" else 0

        while curr_rudeness > c:
            count_a -= 1 if t[l] == "a" else 0
            count_b -= 1 if t[l] == "b" else 0
            curr_rudeness -= count_b if t[l] == "a" else 0
            l += 1

        ans = max(ans, r - l + 1)

    return ans


if __name__ == "__main__":
    n, c = map(int, input().split())
    t = [c for c in input()]
    print(min_rude(t, n, c))
