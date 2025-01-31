n = int(input())

print("? 1 2")
s12 = int(input())
print("? 2 3")
s23 = int(input())
print("? 1 3")
s13 = int(input())

arr = [0] * n
arr[0] = s13 - s23
arr[1] = s12 - arr[0]
arr[2] = s23 - arr[1]
if n == 3:
    print("!", *arr)
    exit(0)
for i in range(4, n + 1):
    print(f"? {i-1} {i}")
    si = int(input())
    arr[i - 1] = si - arr[i - 2]
print("!", *arr)
