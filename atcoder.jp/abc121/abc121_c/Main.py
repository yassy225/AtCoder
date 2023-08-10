#a:値段、b:本数
n,m = map(int, input().split())
l = [list(map(int, input().split())) for l in range(n)]
ans = 0

sorted_l = sorted(l)

for i in range(n):
    if sorted_l[i][1] >= m:
        ans += sorted_l[i][0] * m
        break
    else:
        ans += sorted_l[i][0] * sorted_l[i][1]
        m -= sorted_l[i][1]

print(ans)