# Solution
S = int(input())
J = int(input())
H = int(input())
c = int(input())
s = int(input())
burger = [S, J, H]
drink = [c, s]
arr = []
for i in range(3):
    for j in range(2):
        arr.append(burger[i] + drink[j] - 50)
print(int(min(arr)))
