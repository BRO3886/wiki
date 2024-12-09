# Fair workload

The intuition here is to understand how to convert this into a binary search problem. We need to figure out how to write a mathematical formula that gives us a monotonic predicate function. Using this function, we will find the least maximum value (point of inflexion of F -> T).

In the given question, we can see that the maximum work any worker can do is the sum of all elements in the array (folders). The min work each worker can do is the largest value of folder from the given array of folders. So, for the given example:

```
10 20 30 40 50 60 70 80 90

min work = 90
max work = 450
```

Now, lets say we are hypothetically testing a value k, for which we can divide the folders for different workers. There are two possibilities:

```
f(k) = true, if we are able to divide the folders such that each worker has some folder and all folders are being checked
f(k) = false, if the number of workers fall behind, and the there are still folders remaining.
```

Let's say we start at some value 70. Worker 1 gets [10,20,30], since after 30, it would be more than the capacity we decided (100 > 70). And so on.

```
W1: [10 20 30]
W2: [40]
W3: [50]
```

Now, as we can see, we have exhausted our workers and there are still folders remaining. Hence, 70 is not the correct value. We could go on trying each value linearly, until we have a value for which our division would work. But a faster way would be to binary search on the answer. We can do this by rapidly halving our search space. We already know the min and the max work needed, so, we can rapidly check for any mid between these values.

Again for this mid, we will have twocases based on our monotonic predicate function f(x) (or, f(mid)). If we are able to divide our workers, we will store this value. Now, we know that for any value towards the right of the value - it is possible to have a successful division. But we do not know for sure if this mid is the least maximum value. Hence, we will check the left of this mid. Finally, we will return the least possible value at the end.
