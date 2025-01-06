"""
Question link - https://www.interviewbit.com/problems/subarray-with-given-xor/
TC: O(n)
"""

from typing import List

"""
Key idea: We use prefix XOR property to find subarrays. If Y is current prefix XOR till i,
for any subarray ending at i to have XOR=B, we need prefix XOR X where Y^X=B
So X=Y^B. Count all previous prefix XORs that equal Y^B.
"""


class Solution:
    def solve(self, A: List[int], B: int) -> int:
        prev = 0
        m = {0: 1}
        count = 0
        for i in range(len(A)):
            c = prev ^ A[i]
            if c ^ B in m:
                count += m[c ^ B]
            m[c] = m.get(c, 0) + 1
            prev = c

        return count


if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = int(input())

    print(Solution().solve(a, b))
