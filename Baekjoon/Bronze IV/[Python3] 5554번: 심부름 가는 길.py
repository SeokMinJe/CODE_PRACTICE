# Solution
h2s = int(input())
s2p = int(input())
p2a = int(input())
a2h = int(input())
sum = h2s + s2p + p2a + a2h
print(sum // 60, sum % 60, sep='\n')
