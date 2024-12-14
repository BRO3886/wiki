from typing import List


def checker(transformed: List[int], x: float) -> bool:
    return True


if __name__ == "__main__":
    n, k = list(map(int, input().split(" ")))
    l = []
    for i in range(n):
        ai, bi = list(map(int, input().split(" ")))
        l.append((ai, bi))

    ans = 1e6
    low = 0
    high = 1e6
    err = 1e-6

    for i in range(61):
        mid = (low + high) / 2
        
