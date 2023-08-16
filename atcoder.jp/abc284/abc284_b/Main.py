n = int(input())
ans = []

for _ in range(n):
    t = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(len(a)):
        if a[i] % 2 != 0:
            cnt += 1
    ans.append(cnt)

for j in range(len(ans)):
    print(ans[j])