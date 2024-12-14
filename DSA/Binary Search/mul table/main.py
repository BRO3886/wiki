# question link - https://cses.fi/problemset/task/2422/

def possible(mid, n):
    count = 0
    for i in range(1, n + 1):
        # checking min here since for bigger mids
        # we only need to check upto n elements (num of rows)
        count += min(mid // i, n)

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
