# Binary Search

We reduce the size of our search space at every step into half of size of current search space.

## Time complexity

O(log(n))

![[static/images/bs_tc.png]]

## Requirement for binary search

_Monotonicity_ is required. By monotonicity we mean strictly increasing or strictly decreasing. 

## Predicate functions
These functions return a `true` or `false` for any input. For example:

```
f(x) = true if x > 10 else false. (0 <= x <= inf)

F F F F F F F F F F F  T  T  T  T ....
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14.....

f(x) = true if x is prime else false

1 2 3 4 5 6 7 8 9 10 11
T T T F T F T F F F  F
```

For binary search on predicate functions, we can again consider monotonicity in these functions. In the above example, the first equation is a monotonic predicate function.

```                   
                      M
F F F F F F F F F F F | T T T
```

