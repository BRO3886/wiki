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
