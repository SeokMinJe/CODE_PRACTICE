# Solution
string = str(input())
result = []
for i in range(len(string)):
    if string[i].islower():
        result.append(string[i].upper())
    else:
        result.append(string[i].lower())

for i in range(len(result)):
    print(result[i], end='')
