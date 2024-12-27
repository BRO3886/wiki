# question link - https://codeforces.com/edu/course/2/lesson/6/3/practice/contest/285083/problem/A

from typing import List, Tuple


def check(k: float, ps: List[Tuple[int, int]], n: int) -> bool:
    min_p = -1e9
    max_p = 1e9
    for i in range(n):
        pos, speed = ps[i]
        min_p = max(min_p, pos - (speed * k))
        max_p = min(max_p, pos + (speed * k))
        if min_p > max_p:
            return False

    return True


def solve(ps: List[Tuple[int, int]], n: int) -> float:
    low = 0
    high = 1e9
    ans = 1e9
    for i in range(60):
        mid = (low + high) / 2
        if check(mid, ps, n):
            high = mid
            ans = min(ans, mid)
        else:
            low = mid

    return ans


if __name__ == "__main__":
    n = int(input())
    ps: List[Tuple[int, int]] = [()] * n
    for i in range(n):
        point, speed = list(map(int, input().split()))
        ps[i] = (point, speed)

    print(solve(ps, n))
