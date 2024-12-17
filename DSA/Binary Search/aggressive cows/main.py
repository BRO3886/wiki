from typing import List


def possible(stalls: List[int], dist: int, c: int) -> bool:
    c -= 1
    for i in range(1, n):
        if stalls[i] - stalls[i - 1] >= dist:
            c -= 1
            if c == 0:
                break

    return c == 0


def min_dist(stalls: List[int], n: int, c: int) -> int:
    low = 1
    high = 1e9
    ans = 1e9
    while low <= high:
        mid = (low + high) // 2

        if possible(stalls, mid, c):
            ans = min(mid, ans)
            low = mid + 1
        else:
            high = mid - 1

    return int(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        n, c = list(map(int, input().split()))
        stalls = [0] * n
        for i in range(n):
            stalls[i] = int(input())
        stalls.sort()
        print(min_dist(stalls, n, c))
