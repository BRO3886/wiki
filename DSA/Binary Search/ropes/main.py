from typing import List


def check(val:float, ropes:List[int], k: int)->bool:
    count = 0
    for r in ropes:
        count += r//val
    
    return count >= k

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    ropes = [0] * n
    for i in range(n):
        ropes[i] = int(input())
        
    low = 0
    high = 1e7
    precision = 1e-7
    ans = 0
    for i in range(100):
        mid = (low + high)/2
        if check(mid, ropes, k):
            ans = max(ans, mid)
            low = mid + precision
        else:
            high = mid - precision
            
    print(ans)