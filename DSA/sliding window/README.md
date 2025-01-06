# Sliding Window

The main idea is to reduce the time complexity involved in iterating through the subarray. There could be two types of sliding windows. One fixed size, other dynamic sized (two pointers).

The intuition for identifying sliding window problems is mostly around the phrase - subarrays.

You should consider using sliding window when you notice these patterns in a problem:

- The problem involves sequences (arrays, strings) where you need to find or calculate something among all contiguous subarrays or substrings
- The problem asks for minimum, maximum, longest, shortest, or a specific size
- The problem involves some kind of constraint that must be maintained as you process elements

## Practice Problems

### Find sum of subarray

The intuition here is to smartly update the sum by adding the next element and removing the element not in the window. For example:

```
arr = [1, 2, 3, 4, 5], k = 3

First window: [1, 2, 3], sum = 6
Next window:  [2, 3, 4]
              - To get this sum, we can either:
              - Recalculate: 2+3+4 = 9
              - OR smartly update: 6 + 4 - 1 = 9 (previous sum + new element - first element)

Next window:  [3, 4, 5]
              - Again: 9 + 5 - 2 = 12
```

Code:

```python
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

sum = 0
for i in range(k):
    sum += arr[i]

print(sum, end=" ")

for i in range(k, n):
    sum += arr[i] - arr[i - k]
    print(sum, end=" ")

print()
```

Two loops are not required, can be done in a single loop:

```python
n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += arr[i]

    if i >= k:
        sum -= arr[i-k]

    if i >= k-1:
        print(sum, end=" ")

print()
```

### Find max sum of only distinct elements subarray of size k

The main intuition here is update the answer only when the length or the size of the frequency map is same as k, implying that thre are k distinct elements in the window - if we have k distinct elements, the map will contain exactly k keys. `ans = -1` at the end means no valid window was found.

Example:

```
arr = [1, 1, 2, 1, 3, 2, 1, 1, 2], k = 3

First window [1,1,2]:
- map = {1:2, 2:1}
- len(map) = 2 < k, not valid

Next window [1,2,1]:
- map = {1:2, 2:1}
- len(map) = 2 < k, not valid

Next window [2,1,3]:
- map = {2:1, 1:1, 3:1}
- len(map) = 3 = k, valid! Update ans
```

Code:

```python
testing = False

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    if testing:
        n = 9
        arr = [1, 1, 2, 1, 3, 2, 1, 1, 2]
        k = 3

    sum = 0
    m = {}
    for i in range(k):
        sum += arr[i]
        if m.get(arr[i]):
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1

    ans = -1
    if len(m) == k:
        ans = sum

    for i in range(k, len(arr)):
        sum += arr[i]
        sum -= arr[i - k]
        if m.get(arr[i]):
            m[arr[i]] += 1
        else:
            m[arr[i]] = 1

        m[arr[i - k]] -= 1
        if m[arr[i - k]] == 0:
            del m[arr[i - k]]

        if len(m) == k:
            ans = max(ans, sum)

    if ans == -1:
        print("np")
        exit(0)

    print(ans)
```

> For map, size() function takes log(k) time.

### Print the index of smallest element in all subarrays of size k

A naive approach could be to scan all elements in the window and find the min - TC: `O(nk)`. A better approach here is to benefit from deque such that you are only storing and printing the min for each window. Here, the front of the deque always has the index of the smallest element. We also remove the indexes outside the window.

The time complexity with this approach reduces to O(n) since for each element we are adding and removing once (2n).

Example:

```
arr = 1,2,1,3,1
k = 3

Process [1,2,1]:
- i=0: dq=[0]           (1 added)
- i=1: dq=[0,1]         (2 added)
- i=2: dq=[0,2]         (1 added, removing 1)
Print: 0

Process [2,1,3]:
- dq=[2]                (0 removed as outside window)
- dq=[2,3]              (3 added)
Print: 2

Process [1,3,1]:
- dq=[2,3]              (initial state from previous window)
- dq=[2,4]              (1 added, removing 3 as 1<3)
Print: 2
```

### Find the index of first negative element in all subarrays of size k

Similar as before, we can use a queue to only keep the negative elements of the window, and print the first element of queue. Remove the elements outside the window.

```python
from collections import deque

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    q = deque()

    for i in range(n):
        if arr[i] < 0:
            q.append(i)

        # print(i, q)

        if q and q[0] <= i - k:
            # print("pop", q[0])
            q.popleft()

        if i >= k - 1:
            if q:
                print(arr[q[0]], end=" ")
                # print("p", q[0], q)
            else:
                print(-1, end=" ")
                # print("p", -1, q)
    print()
```

Note that we can also store the element instead of index. Here, the code would change as follows:

```python
from collections import deque

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    q = deque()

    for i in range(n):
        if arr[i] < 0:
            q.append(arr[i])

        # print(i, q)

        if q and i-k >= 0 and arr[i - k] < 0:
            # print("pop", q[0])
            q.popleft()

        if i >= k - 1:
            if q:
                print(q[0], end=" ")
                # print("p", q[0], q)
            else:
                print(-1, end=" ")
                # print("p", -1, q)
    print()

```
