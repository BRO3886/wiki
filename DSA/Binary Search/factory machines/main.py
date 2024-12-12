from typing import List


def possible(seconds: int, max_products: int, machine_times: List[int]) -> bool:
    for mt in machine_times:
        req = seconds
        if mt > req:
            continue
        max_products -= req // mt
    return max_products <= 0


if __name__ == "__main__":
    n, t = list(map(int, input().split(" ")))
    mt = list(map(int, input().split(" ")))

    low, high = 0, int(1e18)
    ans = int(1e18)

    ctr = 1
    while low <= high:
        mid = (low + high) // 2
        if possible(mid, t, mt):
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1
        ctr += 1

    print(ans)
