from typing import List, Tuple


def possible(k: int, segments: List[Tuple[int, int]], n: int) -> bool:
    min_poss, max_poss = 0, 0

    for i in range(n):
        min_poss = max(min_poss - k, segments[i][0])
        max_poss = min(max_poss + k, segments[i][1])

        if not min_poss <= max_poss:
            return False

    return True


def solve(segments: List[Tuple[int, int]], n: int) -> int:
    low = 0
    high = 1e9
    ans = 1e9
    for _ in range(50):
        mid = (low + high) // 2
        if possible(mid, segments, n):
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1

    return int(ans)


if __name__ == "__main__":
    # print(possible(5, [(3, 8), (10, 18), (6, 11)], 3))
    # exit(0)
    t = int(input())
    answers = [0] * t
    for tc in range(t):
        n = int(input())
        segments = [()] * n
        for i in range(n):
            l, r = list(map(int, input().split()))
            segments[i] = (l, r)
        answers[tc] = solve(segments, n)

    for ans in answers:
        print(ans)
