n,m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

sum_a = sum(a)
sorted_a = sorted(a, reverse=True)

for i in range(m):
    if sorted_a[i] >= (sum_a / (4*m)):
        cnt += 1

if cnt == m:
    print("Yes")
else:
    print("No")