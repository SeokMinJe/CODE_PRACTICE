# Solution
arr = []
for i in range(4):
    arr.append(int(input()))

if arr[0] == arr[1] == arr[2] == arr[3]:
    print('Fish At Constant Depth')
elif arr[0] < arr[1] and arr[1] < arr[2] and arr[2] < arr[3]:
    print('Fish Rising')
elif arr[0] > arr[1] and arr[1] > arr[2] and arr[2] > arr[3]:
    print('Fish Diving')
else:
    print('No Fish')
