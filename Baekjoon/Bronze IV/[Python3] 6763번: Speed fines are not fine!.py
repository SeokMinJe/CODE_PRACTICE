# Solution
l = int(input())
r = int(input())

if l >= r:
    print('Congratulations, you are within the speed limit!')
elif l < r:
    F = r - l
    if 0 < F < 21:
        fee = 100
    elif F < 31:
        fee = 270
    else:
        fee = 500
    print('You are speeding and your fine is $%d.' %(fee))
