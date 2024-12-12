def possible(mid, n):
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j * i <= mid:
                count += 1

    return count > (n * n - 1) / 2


if __name__ == "__main__":

    n = int(input())
    low = 0
    high = n * n
    ans = n * n
    while low <= high:
        mid = (low + high) // 2
        if possible(mid, n):
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
