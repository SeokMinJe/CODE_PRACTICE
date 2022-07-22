# Solution
d = input()
l = list(input().split())
num = 0
for i in range(5):
    if d == l[i]:
        num += 1
print(num)
