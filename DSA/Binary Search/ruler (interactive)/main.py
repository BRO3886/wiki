# question link: https://codeforces.com/contest/1999/
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # missing = int(input())
        low = 1
        high = 1000
        ans = 1000
        while low <= high:
            mid = (low + high) // 2
            print("?", mid, mid)
            resp = int(input())

            if resp == mid * mid:
                low = mid + 1
            else:
                ans = min(ans, mid)
                # if ans == missing:
                #     break
                high = mid - 1

        print("!", ans)

        t -= 1
