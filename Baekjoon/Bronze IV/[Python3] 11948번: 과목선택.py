# Solution
A = int(input())
B = int(input())
C = int(input())
D = int(input())
arr1 = list([A, B, C, D])
arr1.remove(min(arr1))

E = int(input())
F = int(input())
arr2 = list([E, F])
print(arr1[0] + arr1[1] + arr1[2] + max(arr2))
