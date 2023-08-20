n = int(input())
a = list(map(int, input().split()))
ans = [] * n

for i in range(n):
    if a[i] != 0:
        a[a[i]-1] = 0

for i in range(n):
    if a[i] != 0:
        ans.append(i+1)

print(len(ans))
print(*ans)