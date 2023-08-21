n = int(input())
s = list([input() for _ in range(n)])
ans = [[] for i in range(n)]

for i in reversed(range(n)):
    for j in range(2*n-1):
        if s[i][j] == '#':
            if (i<n-1 and j>0 and ans[i+1][j-1] == 'X') or \
               (i<n-1 and ans[i+1][j] == 'X') or \
               (i<n-1 and j<2*n-2 and ans[i+1][j+1] == 'X'):
                ans[i].append('X')
                continue
        ans[i].append(s[i][j])

for i in range(n):
    for j in range(2*n-1):
        if ans[i][j] != 0:
            print(ans[i][j], end="")
    print()