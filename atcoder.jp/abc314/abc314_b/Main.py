import sys

n = int(input())
a = [list(map(int, input().split())) for l in range(2*n)]
x = int(input())
hit = []
ans = []

for i in range(1, len(a), 2):
    for j in range(len(a[i])):
        if x == a[i][j]:
            hit.append([len(a[i]), (i+2-1)//2])

if len(hit) == 0:
    print("0")
    print()
    sys.exit()
sorted_hit = sorted(hit)
min_num = min(sorted_hit)

for i in range(len(sorted_hit)):
    if sorted_hit[i][0] == min_num[0]:
        ans.append(sorted_hit[i][1])

print(len(ans))
print(*ans)