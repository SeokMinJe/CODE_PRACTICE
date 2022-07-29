# Solution
arr = list(map(int, input().split()))
t1 = max(arr) + min(arr)
arr.remove(max(arr))
arr.remove(min(arr))
t2 = arr[0] + arr[1]

print(abs(t2 - t1))
