# Solution
n = input()
result = 0
for i in range(len(n)):
    result += int(n[i]) * int(n[i]) * int(n[i]) * int(n[i]) * int(n[i])
print(result)
