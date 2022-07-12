# Solution
X = int(input())
N = int(input())
tmp = 0
for i in range(N):
    a, b = map(int, input().split())
    tmp += a * b

if tmp == X:
    print('Yes')
else:
    print('No')
