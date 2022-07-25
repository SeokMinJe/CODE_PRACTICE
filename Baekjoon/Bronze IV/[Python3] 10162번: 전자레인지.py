# Solution
T = int(input())
A = T // 300
B = (T - A*300) // 60
C = (T - A*300 - B*60) // 10
if (T - A*300 - B*60) % 10 > 0:
    print(-1)
else:
    print(A, B, C)
