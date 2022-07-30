# Solution
dic = {}
dic['bedroom'] = 0
dic['balcony'] = 0
n, cost = map(int, input().split())
for i in range(n):
    size, room = input().split()
    size = int(size)
    if room in dic:
        dic[room] = dic[room] + size
    else:
        dic[room] = size

total = 0
for key in dic:
    total += dic[key]

bedroom = dic['bedroom']
ttl_cost = float((total - dic['balcony']/2)* cost)
print(total)
print(bedroom)
print('%.1f' % ttl_cost)
