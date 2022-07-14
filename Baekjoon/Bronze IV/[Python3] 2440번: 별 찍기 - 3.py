# Solution
N = int(input())
for i in range(1, N+1):
    for _ in range(N+1-i):
        print('*', sep='', end='')
    print('')
