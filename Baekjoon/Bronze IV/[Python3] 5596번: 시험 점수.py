# Solution
a1, a2, a3, a4 = map(int, input().split())
b1, b2, b3, b4 = map(int, input().split())
a = a1 + a2 + a3 + a4
b = b1 + b2 + b3 + b4
if a > b:
    print(a)
else:
    print(b)
