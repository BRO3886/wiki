https://leetcode.com/problems/maximum-subarray/description/
Given an integer array `nums`, find the subarray with the largest sum, and return _its sum_.

```
**Example 1:**

**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6
**Explanation:** The subarray [4,-1,2,1] has the largest sum 6.

**Example 2:**

**Input:** nums = [1]
**Output:** 1
**Explanation:** The subarray [1] has the largest sum 1.

**Example 3:**

**Input:** nums = [5,4,-1,7,8]
**Output:** 23
**Explanation:** The subarray [5,4,-1,7,8] has the largest sum 23.
```

Intuition

Start adding to sum
If the sum becomes negative, start a new calculation of sum
that effectively changes your window size

Code

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = -1e6
        currSum = 0
        for _, num in enumerate(nums):
            currSum += num
            if currSum > currMax:
                currMax = currSum
            if currSum < 0:
                currSum = 0
        return currMax
```

