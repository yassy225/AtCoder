import math

n, d = map(int, input().split())

xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

ans = 0

for i in range(n):
    if(math.sqrt(x[i]*x[i] + y[i]*y[i]) <= d):
        ans += 1

print(ans)