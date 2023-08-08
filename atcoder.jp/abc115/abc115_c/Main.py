n,k = map(int, input().split())
h = [int(input()) for _ in range(n)]
ans = 2 ** 30

sorted_h = sorted(h)

for i in range(n-k+1):
    ans = min(ans, sorted_h[i+k-1] - sorted_h[i])

print(ans)