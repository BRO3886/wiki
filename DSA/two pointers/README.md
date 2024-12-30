# 2 Pointers

Two pointers are problems where we use variable sized sliding windows. It's not a fixed size window, both left and right can move independently. It is useful for a lot of array based problems.

Most of the two pointer problems can be solved with a good segments technique, mentioned later in the article.

> Most two pointer problems can be solved using binary search

## Problem 1

Given 2 sorted arrays of size N and M, for each element in 1st array find number of elements smaller than that in the 2nd array

```
a1 = 1 4 5 9 11
a2 = 2 3 6 7 10

output
0 2 2 4 5
```

**Approach 1:** We can binary search the first number just larger than `a1[i]` and then (len(a2) - j). Time complexity `O(nlogm)` 

Imagine as walls:

```
| 2 3 6 7 10 - [1]
2 3 | 6 7 10 - [4]
2 3 | 6 7 10 - [5]
... and so on
```

Hence, instead of doing binary search, lets say for any `a1[i]` if we know the wall for `a[i-1]` we can run a while loop to find wall for `a1[i]` by starting at wall for `a[i-1]`. A thing to notice is that the total indices the wall can have is overall m distinct places.

```python
a1 = [1,4,5,9,11]
a2 = [2,3,6,7,10]
n = len(a1)
i, j = 0,0
ans = [0]*n
while i < n:
	while j < m and a2[j] < a1[i]:
		j+=1
	ans[i] = j
	i+=1
```

## Good Segments Technique - Type 1

Consider a segment is called "good" if the sum of it's elements is <= k, for all `a[i] >= 1`. For example:

```
a = 1 4 5 9 11
k = 10

[1 4 5] <= 10
so [1 4] <= 10 and [4 5] <= 10
```

That is, all segments enclosed within this "good" segment are also good.

## Problem 2

Given an array of N positive elements, find out the length of the longest subarray with sum <= k.

Example

```
input
a = [10,5,2,7,1,9]
k = 15

output
4 

explanation
subarray is {5,2,7,1}
```

Solution

```python
ans = 0
l, r = 0, 0
n = len(arr)
sum = 0
while r < n:
	while l <= r and sum > k:
		sum -= arr[l]
		l += 1
	sum += arr[r]
	if sum <= k:
		ans = max(ans, r - l + 1)
	r += 1
print(ans)
```

Explanation:
* think around windows
* at every index imagine the subarray ends there
	* 10] (1)
	* 10 5] (2)
	* 10 5 2] (2; 10 is excluded since 17 > 15)
	* and so on
* our answer is the max over all possible answers
* since all elements are > 0, prefix sum is monotonic (strictly increasing)
* left pointer for any index i = r if is at position l, it cannot be possible that for any position i = r+1 the left pointer l = l -1; it can never be smaller because of our type 1 rule; also, prefix sum is monotonic as we proved.
* left pointer only moves ahead
* hence we run a while loop to decrement the sum whenever it becomes > k
* r - l + 1 is done : for ex: [1..100] (100 numbers) - (100 - 1 + 1)
* time complexity: `O(n)` - both l, r move n elements ahead (2n)

## Problem 3

Given an array of N elements find out the length of the longest subarray with number of distinct elements <= k
 
solution

```python
def find(arr: List[int], k: int) -> int:
    ans = 0
    l, r = 0, 0
    n = len(arr)
    sum = 0
    freq = {}
    while r < n:
        if freq.get(arr[r]) == None:
            freq[arr[r]] = 1
        else:
            freq[arr[r]] += 1

        while l <= r and len(freq) > k:
            sum -= arr[l]
            freq[arr[l]] -= 1
            if freq[arr[l]] <= 0:
                del freq[arr[l]]
            l += 1

        sum += arr[r]

        if len(freq) <= k:
            ans = max(ans, r - l + 1)

        r += 1

    return ans
```

Explanation
add here - explain the need for frequency map in relation to the problem statement. Time complexity - O(nlogk) - explain this too

## Good Segments Technique - Type 2

For type 1 - if you have a subarray, and it is good, anything inside it is good. Type 2 on the other hand is opposite. 

Let's say If you have a subarray with sum >= k and `a[i] > 0`. Then, all subarrays containing this subarray will also have the sum > k. In other words, if your segment is good, then all segments enclosing this segment are also good.

For type 1 the question is usually for longest. For type 2 usually* it's shortest type questions - eg, find the smallest subarray with sum >= k.

## Problem 4

Given an array of n components find the length of the shortest subarray with sum >= k.

Solution

```python
def find(arr: List[int], k: int) -> int:
    ans = math.inf
    l = 0
    r = 0
    n = len(arr)
    sum = 0
    while r < n:
        sum += arr[r]
        while l <= r and sum >= k:
            ans = min(ans, r - l + 1)
            sum -= arr[l]
            l += 1
        r += 1
    return ans
```

Explanation
add explanation - explain the inner while loop and how are we moving the left pointer

## Problem 5

Find the number of subarrays with sum <= k, provided that `a[i] > 0`

Solution

```python
def find(arr: List[int], k: int) -> int:
    l = 0
    r = 0
    sum = 0
    n = len(arr)
    count = 0
    while r < n:
        sum += arr[r]
        while sum > k:
            sum -= arr[l]
            l += 1
        if sum <= k:
            count += r - l + 1
        r += 1
    return count
```

Explanation
add explanation - explain how counter compares to the max taken in problem 2

## Problem 6

Count the number of subarrays with sum >=k given that all elements are positive.

Explanation - Approach 1
Please improve this - For any R, if any L is valid, we check for L+1 and so on. For a particular L, we iterate over it on the closest R such that `[L,R]` is good.

```python

def find(arr: List[int], k: int) -> int:
    l = 0
    r = 0
    n = len(arr)
    sum = 0
    count = 0
    while r < n:
        sum += arr[r]
        while l <= r and sum >= k:
            count += n - r
            sum -= arr[l]
            l += 1
        r += 1
    return count

```

Other solution
Total number of subarrays possible: (n*(n+1))/2
Ans: total - subarrays with sum < k
