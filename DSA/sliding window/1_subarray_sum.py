if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += arr[i] 
        
        if i >= k: 
            sum -= arr[i-k]
            
        if i >= k-1:
            print(sum, end=" ")

    print()