n,k = map(int, input().split())
l = list(map(int, input().split()))
ans = 0

l.sort(reverse=True)

for i in range(k):
    ans += l[i]

print(ans)