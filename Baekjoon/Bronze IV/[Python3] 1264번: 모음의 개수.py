# Solution
while(True):
    num = 0
    str = list(input())
    if str[0] == '#' and len(str) == 1:
        break
    for i in range(len(str)):
        if str[i] == 'a' or str[i] == 'A':
            num += 1
        elif str[i] == 'e' or str[i] == 'E':
            num += 1
        elif str[i] == 'i' or str[i] == 'I':
            num += 1
        elif str[i] == 'o' or str[i] == 'O':
            num += 1
        elif str[i] == 'u' or str[i] == 'U':
            num += 1
    print(num)
