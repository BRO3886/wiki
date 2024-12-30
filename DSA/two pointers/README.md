# Two Pointers

## Introduction to Two Pointers

Two pointers is a technique where we use two variables (usually called left and right or i and j) to traverse an array. Unlike fixed sliding windows where the window size remains constant, in two pointers both left and right can move independently. This makes it effective for specific types of problems.

### When to Use Two Pointers

The technique becomes particularly powerful when:

1. You need to find a relationship between elements

   - Like finding pairs that sum to a target
   - Similar to how you might use two fingers to find matching socks in a drawer

2. You're working with sorted arrays

   - The sorted property lets you make decisions about which pointer to move
   - Like using two bookmarks to find where two different chapters overlap

3. You need to track subarrays or subsequences

   - Similar to how you might use two fingers to measure a section of ribbon

4. You're dealing with palindromes or symmetric patterns
   - Like comparing letters from both ends of a word to check if it reads the same backward

## Problem Set 1: Basic Two Pointers

### Problem 1: Count Smaller Elements

**Problem Statement:**  
Given two sorted arrays A and B, for each element in A, find the count of elements in B that are smaller than it.

**Example:**

```
Input:
A = [1, 4, 5, 9, 11]  // First sorted array
B = [2, 3, 6, 7, 10]  // Second sorted array

Output: [0, 2, 2, 4, 5]

Explanation:
- For A[0] = 1: No elements in B are smaller (count = 0)
- For A[1] = 4: Elements {2, 3} are smaller (count = 2)
- For A[2] = 5: Elements {2, 3} are smaller (count = 2)
- For A[3] = 9: Elements {2, 3, 6, 7} are smaller (count = 4)
- For A[4] = 11: Elements {2, 3, 6, 7, 10} are smaller (count = 5)
```

**Building Intuition:**
Let's understand how we can solve this efficiently. Consider what happens as we process each element:

Let's understand the core optimization by looking at how we process elements sequentially:

Consider these arrays:

```
A = [1, 4, 7, 9, 11]
B = [2, 3, 6, 7, 10]
```

When we process A[1] = 4:

1. We've counted elements up to some position j in B (where we found the first element ≥ 4)
2. In this case, we stopped at B[2] because 6 > 4, after counting {2, 3}

Now for A[2] = 7:

1. Since A is sorted, 7 > 4, we can start from where we left off (position 2 in B)
2. We find B[2] = 6 < 7, so we count it and move forward
3. We find B[3] = 7 ≥ 7, so we stop here

This demonstrates a crucial property: For each new element in A, we never need to move backwards in B. We may need to move forward more positions in B for larger elements in A, but we never need to recheck elements we've already processed. Why? Because:

1. A is sorted, so each new element is larger than the previous one
2. B is sorted, so once we've counted elements smaller than A[i], they're definitely smaller than A[i+1]
3. Therefore, we can always continue our scan of B from where we previously stopped

**The "Wall" Visualization:**
Imagine B as a row of increasing heights:

```
B: [2  3  6  7  10]
   ^
   wall for A[0]=1

B: [2  3  6  7  10]
         ^
   wall for A[1]=4
```

The "wall" represents where we stop counting. For each element in A:

1. The wall can only move right (because A is sorted)
2. Everything before the wall is smaller than our current element
3. We don't need to rebuild the wall from scratch each time

This visual model helps us understand why our solution works in O(n) time instead of O(n²).

**Solution with Explained Intuition:**

```python
def countSmallerElements(A: List[int], B: List[int]) -> List[int]:
    n, m = len(A), len(B)
    i, j = 0, 0  # i tracks A, j is our "wall" in B
    result = [0] * n

    while i < n:
        # j is already at the right position for elements smaller than A[i-1]
        # we just need to move it forward if needed for A[i]
        while j < m and B[j] < A[i]:
            j += 1
        result[i] = j  # j represents how many elements we've passed
        i += 1

    return result
```

**Mental Model for Time Complexity:**
Why is this O(n + m) and not O(n \* m)?

- Think of pointer j as walking along array B
- It never steps backward
- Even though we have a nested while loop, j can only move right m times total
- i moves right n times
- Total steps = n + m

## Good Segments Technique

The Good Segments Technique is about understanding how properties of subarrays relate to their containing or contained subarrays. Let's build this understanding from the ground up.

### Type 1: The "Inheritance Down" Property

Imagine you have a rope with weights tied to it at different points. If you can lift a section of the rope (it's not too heavy), you can definitely lift any smaller section within it.

This is Type 1: If a segment is "good", all segments within it are also "good".

**Real-world analogy:**
Think of a hiking trail. If you can walk a 5-mile section of the trail (it's not too steep), you can definitely walk any 2-mile section within those 5 miles. The property of "being walkable" passes down to smaller segments.

Examples of Type 1 properties:

1. Sum ≤ K (if a segment sums to less than K, any part of it also sums to less than K)
2. Maximum element ≤ K (if no element in a segment exceeds K, this is true for any subsegment)
3. Number of distinct elements ≤ K (if a segment has at most K distinct elements, any subsegment will have at most K distinct elements)

### Type 2: Property That Extends to Larger Segments

Think of holding a basketball at 7 feet high - if you can reach that height, adding a platform under your feet will only make the ball go higher, never lower. Similarly, Type 2 properties are those that, once achieved, can't be "undone" by adding more elements.

A Type 2 property means: if any segment has the property, then expanding that segment (making it larger by including more elements) will preserve that property.

For example, if we're looking for segments with sum ≥ K:

```
Array: [2, 5, 1, 3]
K = 7

If we find segment [5, 1] with sum = 6:
- Not good yet (6 < 7)

If we find segment [5, 1, 3] with sum = 9:
- Good because 9 ≥ 7
- Adding elements before: [2, 5, 1, 3] sum = 11 ≥ 7 (still good)
- Any segment containing [5, 1, 3] must have sum ≥ 7
```

Examples of Type 2 properties:

1. Sum ≥ K (adding more numbers only increases the sum)
2. Contains element K (adding more elements can't remove K from the segment)
3. Maximum element ≥ K (adding more elements can't decrease the maximum)

### Problem 2: Longest Subarray with Sum ≤ K

Given an array of positive numbers and a value K, we need to find the length of the longest subarray whose sum is less than or equal to K.

Let's start with the example:

```
Array = [10, 5, 2, 7, 1, 9]
K = 15

Output = 4
Explanation: Subarray [5, 2, 7, 1] has sum = 15 which is ≤ K
```

This is a Type 1 problem because of how sums behave with positive numbers. When a larger segment satisfies our condition (sum ≤ K), any smaller segment within it must also satisfy this condition. Let's see why:

Take a segment that works, say [5, 2, 7, 1] with sum = 15:

- If we take [5, 2, 7], sum = 14 ≤ 15
- If we take [2, 7, 1], sum = 10 ≤ 15
- If we take [5, 2], sum = 7 ≤ 15

This is true because when all numbers are positive, removing elements can only decrease the sum. Therefore, any subsegment of a valid segment must also be valid.

**Building Solution Intuition:**

Let's solve a small example by hand:

```
Array: [3, 1, 2, 4, 1]
K = 6
```

First, let's understand what we're looking for:

1. We want the longest subarray
2. Its sum should not exceed 6
3. Since all numbers are positive, adding a number always increases the sum

Now, imagine building all possible subarrays ending at each position:

For index 0 (element = 3):

```
[3] = 3 ≤ 6 ✓
```

For index 1 (element = 1):

```
[1] = 1 ≤ 6 ✓
[3,1] = 4 ≤ 6 ✓
```

For index 2 (element = 2):

```
[2] = 2 ≤ 6 ✓
[1,2] = 3 ≤ 6 ✓
[3,1,2] = 6 ≤ 6 ✓
```

Key insights:

1. When we add a new element, we only need to check subarrays ending at that element
2. If a sum becomes too large, removing elements from the left can only help
3. We don't need to try removing elements from the middle (why? because of Type 1!)

This leads to our two-pointer solution:

```python
def longestSubarrayWithSum(arr: List[int], k: int) -> int:
    longest = 0
    left = right = 0
    current_sum = 0

    while right < len(arr):
        # Grow the window
        current_sum += arr[right]

        # Shrink from left if sum exceeds K
        while left <= right and current_sum > k:
            current_sum -= arr[left]
            left += 1

        # Current window is valid, update longest
        if current_sum <= k:
            longest = max(longest, right - left + 1)

        right += 1

    return longest
```

**Why this works - deeper understanding:**

1. Why don't we need to try all possible subarrays?

   - If sum[l:r] ≤ K, all subarrays within it are ≤ K (Type 1)
   - If sum[l:r] > K, all subarrays containing it are > K
   - Therefore, for each right position, we only need the leftmost valid left position

2. Why move the left pointer forward only?
   - Because of monotonicity: if sum[l:r] > K, sum[l:r+1] will also be > K
   - Any valid window must start after the leftmost invalid position

### Problem 3: Longest Subarray with at Most K Distinct Elements

Given an array and a value K, find the length of the longest subarray that contains at most K distinct elements.

Before diving into the solution, let's understand what makes this a two pointer problem. When we have a valid window (a subarray with at most K distinct elements), adding more elements might make it invalid, and we'll need to shrink it from the left. This pattern of growing and shrinking a window suggests a two pointer approach.

#### Example

```
Array: [1, 2, 1, 2, 3, 3, 4]
K = 2

Output: 4
Explanation: The subarray [1, 2, 1, 2] contains only 2 distinct elements (1 and 2)
```

#### Understanding the Challenge

Let's walk through what happens as we process this array:

```
[1] → 1 distinct element
[1, 2] → 2 distinct elements
[1, 2, 1] → still 2 distinct (1 was already seen)
[1, 2, 1, 2] → still 2 distinct
[1, 2, 1, 2, 3] → 3 distinct (exceeds K)
```

We face two key challenges:

1. How do we efficiently track the number of distinct elements in our current window?
2. When we remove an element from the left, how do we know if it was the last occurrence of that element in our window?

This is where a frequency map becomes essential. The frequency map serves two purposes:

1. Its size (number of keys) tells us how many distinct elements we have
2. The frequency values tell us when we can completely remove an element

#### Solution with Explanation

```python
def longestSubarrayKDistinct(arr: List[int], k: int) -> int:
    longest = 0          # Track the longest valid window seen
    left = right = 0     # Our two pointers
    freq = {}           # Map to track frequency of each element

    while right < len(arr):
        # Add new element to our window
        if arr[right] not in freq:
            freq[arr[right]] = 1
        else:
            freq[arr[right]] += 1

        # While window has too many distinct elements
        while len(freq) > k:
            # Remove elements from the left
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]  # Remove if it was the last occurrence
            left += 1

        # Current window is valid, update longest
        longest = max(longest, right - left + 1)
        right += 1

    return longest
```

#### Step-by-Step Example

Let's process our example array [1, 2, 1, 2, 3, 3, 4] with K = 2:

```
Step 1: right = 0
Window: [1]
Freq: {1: 1}
Distinct = 1 ≤ 2 → longest = 1

Step 2: right = 1
Window: [1, 2]
Freq: {1: 1, 2: 1}
Distinct = 2 ≤ 2 → longest = 2

Step 3: right = 2
Window: [1, 2, 1]
Freq: {1: 2, 2: 1}
Distinct = 2 ≤ 2 → longest = 3

Step 4: right = 3
Window: [1, 2, 1, 2]
Freq: {1: 2, 2: 2}
Distinct = 2 ≤ 2 → longest = 4

Step 5: right = 4
Window: [1, 2, 1, 2, 3]
Freq: {1: 2, 2: 2, 3: 1}
Distinct = 3 > 2
   → Remove from left until valid
   → After removing [1], still 3 distinct
   → After removing [2], still 3 distinct
   → After removing [1], window becomes [2, 2, 3]
   Freq: {2: 2, 3: 1}
   Distinct = 2 ≤ 2
```

### Why the Frequency Map?

You might wonder why we don't just use a set to track distinct elements. Consider this scenario:

```
Window: [1, 2, 1]
If we remove the first 1, we still have another 1 in our window
A set wouldn't tell us this, but our frequency map shows {1: 2, 2: 1}
```

The frequency map lets us:

1. Add elements by incrementing their frequency
2. Remove elements by decrementing their frequency
3. Know exactly when an element is completely removed (frequency becomes 0)
4. Get the distinct count via len(freq)

#### Time and Space Complexity

Time Complexity: O(nlogk)
Let's break this down:

1. Window Operations:

   - Each element is added exactly once (right pointer)
   - Each element is removed at most once (left pointer)
   - This gives us O(n) window operations

2. Map Operations:

   - In most implementations (like in C++ or Python), map/dictionary operations are O(logk) in worst case
   - Each time we add or remove an element, we need to modify the map
   - We also check the size of the map (len(freq)) which requires traversing the tree structure
   - Since our map never grows beyond k size (we ensure this by shrinking the window), each operation is O(logk)

3. Total Complexity:
   - For each of our O(n) window operations
   - We perform O(logk) map operations
   - Therefore, total complexity is O(nlogk)

Space Complexity: O(k)

- The frequency map stores at most k elements (since we shrink the window when we exceed k distinct elements)
- Each map entry stores an element and its frequency

#### Edge Cases to Consider

1. Empty array → return 0
2. K = 1 → longest sequence of same element
3. K ≥ array length → entire array
4. K = 0 → return 0

#### Key Insights

1. This is a Type 1 problem: if a window has ≤ K distinct elements, any part of it also has ≤ K distinct elements
2. We never need to remove elements from the middle of the window
3. The frequency map efficiently handles both counting distinct elements and tracking multiple occurrences

### Problem 4: Finding Shortest Subarray with Sum ≥ K

Given an array of positive numbers and a target value K, find the length of the shortest subarray whose sum is greater than or equal to K.

#### Understanding Why This is a Type 2 Problem

This problem exhibits the Type 2 property: if a subarray's sum is ≥ K, any larger array containing it must also have sum ≥ K. This happens because all elements are positive, so adding more elements can only increase the sum.

Consider a simple example to understand this property:

```
Array = [3, 1, 4, 2]
K = 5

If we find [1, 4] has sum = 5 ≥ K:
Then [3, 1, 4] must have sum > K (8 ≥ 5)
And [1, 4, 2] must have sum > K (7 ≥ 5)
And [3, 1, 4, 2] must have sum > K (10 ≥ 5)
```

#### Solution Development

Let's look at a complete example:

```
Array = [2, 3, 1, 2, 4, 3]
K = 7
```

When we process this array, at each step we want to:

1. Extend our window until we find a valid sum (≥ K)
2. Once we have a valid sum, try to minimize it by removing elements from the left
3. Record the length if it's shorter than what we've seen

Let's walk through this process:

```
Initial window: [2]
Sum = 2 < 7, need more elements

Window: [2, 3]
Sum = 5 < 7, need more elements

Window: [2, 3, 1]
Sum = 6 < 7, need more elements

Window: [2, 3, 1, 2]
Sum = 8 ≥ 7
Can we do better? Remove 2 from left:
  Window: [3, 1, 2]
  Sum = 6 < 7, can't remove more
Length = 4

Window: [2, 3, 1, 2, 4]
Sum = 12 ≥ 7
Remove from left:
  [3, 1, 2, 4] → sum = 10 ≥ 7
  [1, 2, 4] → sum = 7 ≥ 7
  [2, 4] → sum = 6 < 7
Length = 3

Window: [2, 3, 1, 2, 4, 3]
Sum = 15 ≥ 7
Remove from left until minimal...
Final length = 2 ([4, 3])
```

#### Solution Implementation

```python
def shortestSubarray(arr: List[int], k: int) -> int:
    shortest = float('inf')  # Initialize to infinity
    left = right = 0
    current_sum = 0

    while right < len(arr):
        # Add element to window
        current_sum += arr[right]

        # Try to minimize window while keeping sum ≥ k
        while left <= right and current_sum >= k:
            shortest = min(shortest, right - left + 1)
            current_sum -= arr[left]
            left += 1

        right += 1

    return shortest if shortest != float('inf') else 0
```

#### Why This Works - Detailed Analysis

The solution's correctness relies on several key insights:

1. Optimality of Left Pointer Movement:
   When we find a valid window, why is it safe to remove elements from the left?

   - If we have a valid window [l...r]
   - And removing elements from left still gives sum ≥ K
   - Then the shorter window must be better (we want minimum length)

2. No Backtracking Needed:
   Why don't we need to consider elements we removed?

   - Once we remove element at position l
   - For any future right pointer position
   - Including l would only make the window longer
   - And we already know we can achieve sum ≥ K without it

3. Monotonic Property:
   The solution works because of two monotonic properties:
   - Adding elements can only increase the sum (all numbers positive)
   - Moving right pointer forward ensures we process each starting point exactly once

#### Time Complexity Analysis

Time Complexity: O(n)

- Each element is added exactly once (right pointer)
- Each element is removed at most once (left pointer)
- Both pointers only move forward
- Total operations = O(2n) = O(n)

Space Complexity: O(1)

- We only store a few variables regardless of input size

#### Edge Cases and Special Considerations

1. Empty array → return 0
2. All elements sum to less than K → return 0
3. Single element ≥ K → return 1
4. No valid subarray exists → return 0

#### Key Takeaways

1. This is a Type 2 problem: if a window works, any larger window containing it works
2. Once we find a valid sum, we can safely minimize from the left
3. We never need to consider elements we've removed for future windows
4. Both pointers move monotonically forward, giving us linear time complexity

## Counting Valid Subarrays: A Deep Dive

### Introduction to Counting Problems

In our previous problems, we focused on finding the longest or shortest valid subarrays. Now we'll tackle a different challenge: counting all valid subarrays. This introduces new complexities because we need to count every valid subarray, not just find the optimal one.

### Problem 5: Count Subarrays with Sum ≤ K

Given an array of positive numbers and a value K, count the number of subarrays whose sum is less than or equal to K.

#### Understanding the Problem

Let's start with a simple example to understand what we're counting:

```
Array = [1, 2, 3]
K = 3

Valid subarrays:
[1] = 1
[2] = 2
[3] = 3
[1, 2] = 3

Total count = 4
```

This is a Type 1 problem: if a sum is ≤ K, any part of it is also ≤ K. This property lets us count efficiently.

#### Key Insight for Counting

When we find a valid window [l...r], how many subarrays ending at position r does it contribute? The answer is (r - l + 1) because every subarray ending at r and starting at any position from l to r is valid.

Let's understand this with an example:

```
Array = [1, 2, 1]
K = 3

At r = 0:
  Window: [1]
  Sum = 1 ≤ 3
  Valid subarrays ending at 0: [1]
  Count += 1

At r = 1:
  Window: [1, 2]
  Sum = 3 ≤ 3
  Valid subarrays ending at 1: [2], [1,2]
  Count += 2

At r = 2:
  Window: [1, 2, 1]
  Sum = 4 > 3
  Shrink: [2, 1]
  Sum = 3 ≤ 3
  Valid subarrays ending at 2: [1], [2,1]
  Count += 2

Total count = 5
```

#### Solution Implementation

```python
def countSubarrays(arr: List[int], k: int) -> int:
    count = 0
    left = 0
    current_sum = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while left <= right and current_sum > k:
            current_sum -= arr[left]
            left += 1

        if current_sum <= k:
            count += right - left + 1

    return count
```

### Problem 6: Count Subarrays with Sum ≥ K

Now let's flip the condition: count subarrays with sum greater than or equal to K. This is a Type 2 problem.

#### Understanding the Difference

The key difference from Problem 5 is how we count when we find a valid window. When a window [l...r] has sum ≥ K, all windows containing this window will also have sum ≥ K.

Let's look at an example:

```
Array = [1, 4, 2]
K = 4

When we find [4] with sum = 4:
- It contributes [4]
- Future elements will create more valid arrays: [4,2]
- Previous elements also create valid arrays: [1,4]
- And combinations of both: [1,4,2]
```

#### Key Insight for Counting

When we find a valid window ending at position r, how many total subarrays will it contribute to? For each valid left pointer position l, we'll get valid subarrays starting anywhere from 0 to l and ending at r.

```
Array = [1, 4, 2]
K = 4

At r = 1 (element 4):
  Valid window: [4]
  This means [4] and [1,4] are valid
  Count += 2 (number of positions before r + 1)

At r = 2 (element 2):
  Valid windows: [4,2]
  This means [4,2] and [1,4,2] are valid
  Count += 2
```

#### Solution Implementation

```python
def countSubarraysGreaterEqual(arr: List[int], k: int) -> int:
    count = 0
    left = 0
    current_sum = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while left <= right and current_sum >= k:
            count += len(arr) - right  # Key difference in counting
            current_sum -= arr[left]
            left += 1

    return count
```

### Comparing the Two Problems

Both problems involve counting subarrays, but they differ in crucial ways:

1. Counting Strategy:

   - Sum ≤ K: When we find a valid window, we count subarrays ending at the current position
   - Sum ≥ K: When we find a valid window, we count all possible extensions of this window

2. Window Management:

   - Sum ≤ K: We maintain a maximal valid window and count based on its size
   - Sum ≥ K: We find minimal valid windows and count all ways to extend them

3. Time Complexity:
   Both solutions achieve O(n) because:
   - Each element is added once
   - Each element is removed at most once
   - Counting operations are constant time

### Key Lessons

1. When counting subarrays, we need to:

   - Identify what makes a subarray valid
   - Determine how many valid subarrays each window contributes
   - Count efficiently without double-counting

2. The type of problem (Type 1 or Type 2) determines:

   - How we manage our window
   - How we count valid subarrays
   - Which subarrays a valid window guarantees

3. Despite different counting strategies, both problems maintain linear time complexity through careful window management.
