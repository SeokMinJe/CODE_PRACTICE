# Solution
while(1):
    n = float(input())
    if n == 0:
        break
    else:
        sum = n**4 + n**3 + n**2 + n*1 + 1
        print('%.2f' % sum)
