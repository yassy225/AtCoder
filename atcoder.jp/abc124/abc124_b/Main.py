n = int(input())
h = list(map(int, input().split()))

ans = 1

for i in range(1,n):
    mnt = max(h[:i])
    if h[i] >=  mnt:
        ans += 1

print(ans)