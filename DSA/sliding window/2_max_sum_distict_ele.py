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
