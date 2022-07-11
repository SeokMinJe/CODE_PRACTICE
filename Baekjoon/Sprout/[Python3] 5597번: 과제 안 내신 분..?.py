# Solution
arr = []
ttl = []

for i in range(28):
    arr.append(int(input()))

for i in range(1, 31):
    ttl.append(i)

for i in range(len(arr)):
    if arr[i] in ttl:
        ttl.remove(int(arr[i]))

if ttl[0] > ttl[1]:
    print(ttl[1])
    print(ttl[0])
else:
    print(ttl[0])
    print(ttl[1])
