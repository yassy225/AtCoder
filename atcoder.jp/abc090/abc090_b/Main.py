a,b = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    i = str(i)
    if i == "".join(reversed(i)):
        cnt += 1

print(cnt)