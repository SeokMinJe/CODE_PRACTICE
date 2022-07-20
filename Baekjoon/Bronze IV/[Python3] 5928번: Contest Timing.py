# Solution
arr = []
for i in range(5):
    tmp = int(input())
    if tmp < 40:
        arr.append(40)
    else:
        arr.append(tmp)

print(sum(arr) // 5)
