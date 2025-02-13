https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

```
Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
### Intuition
- -ve * -ve can give positive - max product also
- at each step keep track of min such that when `currMin * nums[idx] ` becomes max `currPrd` takes that value
### Code
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currPrd = 1
        currMin = 1
        for i in range(len(nums)):
            temp = currPrd * nums[i]
            currPrd = max(temp, currMin * nums[i], nums[i])
            currMin = min(temp, currMin * nums[i], nums[i])
            if currPrd > currMax:
                currMax = currPrd
        return currMax
```