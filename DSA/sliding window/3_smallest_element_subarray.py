from collections import deque

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

# Deque will store indices, but in a way that elements are increasing
dq = deque()

# Process first k elements (first window)
for i in range(k):
    # Remove elements greater than current from back
    while dq and arr[i] < arr[dq[-1]]:
        dq.pop()
    dq.append(i)

# Print index of min element in first window
print(dq[0], end=" ")

# Process rest of the elements
for i in range(k, n):
    if dq and dq[0] <= i - k:
        dq.popleft()

    # Remove elements greater than current from back
    while dq and arr[i] < arr[dq[-1]]:
        dq.pop()
    dq.append(i)

    print(dq[0], end=" ")

print()
