# question link - https://codeforces.com/problemset/problem/1166/C
from bisect import bisect_right

if __name__ == "__main__":
    n = int(input())
    points = list(map(int, input().split()))
    points = sorted([abs(x) for x in points])

    ans = 0
    for i in range(len(points)):
        count = bisect_right(points, 2 * points[i])
        ans += count - 1 - i

    print(ans)
