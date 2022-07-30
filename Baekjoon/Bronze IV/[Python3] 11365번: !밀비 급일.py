# Solution
while(1):
    str = input()
    if str == 'END':
        break
    else:
        l = len(str)
        for i in range(l):
            print(str[l - i - 1], end='')
        print('')
