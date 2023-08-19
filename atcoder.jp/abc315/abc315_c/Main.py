n = int(input())
a = [[] for _ in range(n)]
ans = 0

for i in range(n):
    f,s = map(int, input().split())
    a[f-1].append(s)

b = []
for i in range(n):
    if a[i]:
        a[i].sort(reverse=True)
        #同じ味のとき
        if len(a[i]) >= 2:
            ans = max(ans, a[i][0] + a[i][1] // 2)
        b.append(a[i][0])

#違う味のとき
b.sort(reverse=True)
if len(b) >= 2:
    ans = max(ans, b[0] + b[1])

print(ans)