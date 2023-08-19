n = int(input())
l = list(map(int, input().split()))
cnt = 0

sorted_l = sorted(l)

for i in range(n-2):
    for j in range(i+1, n-1):
        if sorted_l[i] == sorted_l[j]:
            continue
        for k in range(j+1, n):
            if sorted_l[j] == sorted_l[k]:
                continue
            if sorted_l[i] + sorted_l[j] > sorted_l[k]:
                cnt += 1
print(cnt)