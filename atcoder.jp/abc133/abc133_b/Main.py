import math

n,d = map(int, input().split())
x = [list(map(int, input().split())) for l in range(n)]
cnt = 0

for i in range(n-1):
    for j in range(1+i,n):
        ans = 0
        for k in range(d):
            ans += (x[i][k] - x[j][k]) ** 2
        if math.sqrt(ans).is_integer():
            cnt += 1
print(cnt)