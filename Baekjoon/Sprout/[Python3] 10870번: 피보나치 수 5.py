# Solution 
n = int(input())
arr = [0, 1]

def fibo(arr, i):
    arr.append(arr[i] + arr[i+1])

for i in range(n):
    fibo(arr, i)
print(arr[n])
