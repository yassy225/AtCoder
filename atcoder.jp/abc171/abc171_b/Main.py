n,k = map(int, input().split())
p = list(map(int, input().split()))

sorted_p = sorted(p)
ans = 0

for i in range(k):
    ans += sorted_p[i]

print(ans)