m = int(input())
d = list(map(int, input().split()))
cnt = 0
day = 0
month = 0

middle_day = (sum(d)+1) // 2

for i in range(len(d)):
    cnt += d[i]
    if cnt >= middle_day:
        month = i
        cnt -= d[i]
        break

print(month+1, end=" ")
print(middle_day - cnt)