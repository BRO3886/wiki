"""
Question link - https://codeforces.com/edu/course/2/lesson/9/3/practice/contest/307094/problem/F
"""

from typing import List


def substrings_with_cards(s: List[str], cards: List[str], n: int, m: int) -> int:
    ans = 0
    l, r = 0, 0
    freq_map = {}

    for card in cards:
        if freq_map.get(card) is None:
            freq_map[card] = 1
        else:
            freq_map[card] += 1

    copy_map = freq_map.copy()

    while r < n:
        if s[r] not in copy_map:
            l = r + 1
            r += 1
            copy_map = freq_map.copy()  # reset
            continue

        copy_map[s[r]] -= 1

        while l <= r and copy_map.get(s[r]) < 0:
            copy_map[s[l]] += 1
            l += 1

        ans += r - l + 1
        r += 1

    return ans


if __name__ == "__main__":
    n, m = map(int, input().split())
    s = [c for c in input()]
    cards = [c for c in input()]

    print(substrings_with_cards(s, cards, n, m))
