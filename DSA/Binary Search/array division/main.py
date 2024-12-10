import math
from typing import List


def possible(val, arr, k):
    used_divs = 1
    curr_total = 0
    for v in arr:
        if curr_total + v <= val:
            curr_total += v
        else:
            if used_divs == k:
                return False
            if v > val:
                return False
            used_divs += 1
            curr_total = v
    return True


def bsearch(arr: List[int], k: int) -> int:
    low, high = 0, int(1e19)
    ans = int(1e19)
    while low <= high:
        mid = (low + high) // 2
        if possible(mid, arr, k):
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1
    return ans


if __name__ == "__main__":
    line1 = input()
    n, k = list(map(int, line1.split(" ")))
    arr = list(map(int, input().split(" ")))
    print(bsearch(arr, k))
