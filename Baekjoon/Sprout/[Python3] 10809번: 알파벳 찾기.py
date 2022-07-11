# Solution
from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)
S = str(input())
arr = []
for i in range(len(alphabet_list)):
    if alphabet_list[i] in S:
        arr.append(S.find(alphabet_list[i]))
    else:
        arr.append(-1)

for i in arr:
    print(i, end=' ')
