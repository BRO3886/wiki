"""
Question link - https://www.interviewbit.com/problems/subarray-with-given-xor/
TC: O(n)
"""

from typing import List


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
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
