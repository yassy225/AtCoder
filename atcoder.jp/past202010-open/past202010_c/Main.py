n,m = map(int, input().split())
s = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        ans = 0
        if s[i][j] == '#':
            ans += 1
        #上
        if i>0 and s[i-1][j] == '#':
            ans += 1

        #下
        if i<n-1 and s[i+1][j] == '#':
            ans += 1

        #左
        if j>0 and s[i][j-1] == '#':
            ans += 1

        #右
        if j<m-1 and s[i][j+1] == '#':
            ans += 1

        #左上
        if j>0 and i>0 and s[i-1][j-1] == '#':
            ans += 1

        #右上
        if j<m-1 and i>0 and s[i-1][j+1] == '#':
            ans += 1

        #右下
        if j<m-1 and i<n-1 and s[i+1][j+1] == '#':
            ans += 1

        #左下
        if j>0 and i<n-1 and s[i+1][j-1] == '#':
            ans += 1

        print(ans,end="")
    print()